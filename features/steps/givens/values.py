import itertools

import utils.geometry
from validation_handling import full_stack_rule, gherkin_ifc
from . import ValidationOutcome, OutcomeSeverity

@gherkin_ifc.step("Its values")
@gherkin_ifc.step("Its values excluding {excluding}")
def step_impl(context, inst, excluding=None):
    yield ValidationOutcome(inst=inst.get_info(recursive=True, include_identifier=False, ignore=excluding),
                            severity=OutcomeSeverity.PASSED)


@gherkin_ifc.step("The values grouped pairwise at depth {ignored:d}")
def step_impl(context, inst, ignored=0):
    inst = itertools.pairwise(inst)
    yield ValidationOutcome(inst=inst, severity=OutcomeSeverity.PASSED)

@gherkin_ifc.step("The determinant of the placement matrix")
def step_impl(context, inst):
    import numpy as np
    import ifcopenshell.ifcopenshell_wrapper

    if inst.wrapped_data.file_pointer() == 0:
        # In some case we're processing operations on attributes that are 'derived in subtype', for
        # example the Operator on an IfcMirroredProfileDef. Derived attribute values are generated
        # on the fly and are not part of a file. Due to a limitation on the mapping expecting a file
        # object, such instances can also not be mapped. Therefore in such case we create a temporary
        # file to add the instance to.
        f = ifcopenshell.file(schema=context.model.schema_identifier)
        inst = f.add(inst)

    shp = ifcopenshell.ifcopenshell_wrapper.map_shape(ifcopenshell.geom.settings(), inst.wrapped_data)
    d = np.linalg.det(np.array(shp.components))
    yield ValidationOutcome(inst=d, severity=OutcomeSeverity.PASSED)


@gherkin_ifc.step(u"the instances '{n_steps:d}' steps up")
@full_stack_rule
def step_impl(context, inst, path, n_steps : int):
    """Replaces the input instance with the value higher up in the execution. Note that this only applies to input
    instances that are still present at execution time during the current step, it doesn't overwrite replace the full
    set of instances from before, only those that are still active currently.

    Args:
        n_steps (int): Number of steps to look upwards in execution
    """
    yield ValidationOutcome(inst = path[::-1][n_steps-1], severity = OutcomeSeverity.PASSED)


@gherkin_ifc.step("the [{edges_or_points}] of .{attribute_containing_geometry}.")
def step_impl(context, inst, edges_or_points, attribute_containing_geometry):
    """
    Returns the edges or points of the geometry stored in the attribute indicated by 'attribute_containing_geometry'.
    This implementation was initially developed to support SWE003 for IfcSectionedSolidHorizontal.
    The flexibility to specify a particular attribute is designed for other entity types relevant to infrastructure sweeps along alignments - such as IfcSectionedSurface.
    """
    geom_inst_container = getattr(inst, attribute_containing_geometry)
    profiles = tuple(utils.geometry.get_profile_curve(gi) for gi in geom_inst_container)
    def extract_geometry(item):
        """
        Recursively extract geometry, preserving nesting structure
        """
        if isinstance(item, (tuple, list)):
            return tuple(extract_geometry(sub_item) for sub_item in item)
        else:
           if edges_or_points.upper() == "EDGES":
               return utils.geometry.get_edges(context.model, item)
           elif edges_or_points.upper() == "POINTS":
               return utils.geometry.get_points(context.model, item)
           else:
               raise ValueError(f"Invalid value for edges_or_points: {edges_or_points}")

    if edges_or_points.upper() in ("EDGES", "POINTS"):
        geometry = extract_geometry(profiles)
        yield ValidationOutcome(inst=geometry, severity=OutcomeSeverity.PASSED)
    else:
        raise ValueError(f"Invalid value for edges_or_points: {edges_or_points}")


@gherkin_ifc.step("the number of [{edges_or_points}]")
def step_impl(context, inst, edges_or_points):
    ep = edges_or_points.upper()
    if ep in ("EDGES", "POINTS"):
        def count_collection(item):
            if isinstance(item, (tuple, list)):
                return tuple(count_collection(sub_item) for sub_item in item)
            elif isinstance(item, (frozenset, set)):
                return len(item)
            else:
                return len(item)
        count = count_collection(inst)
        yield ValidationOutcome(inst=count, severity=OutcomeSeverity.PASSED)
    else:
        raise ValueError(f"Invalid value for edges_or_points: {edges_or_points}")
