# IBP002 - Alignment Contains Business Logic and Representation

These tests validate that an alignment contains both business logic and representation.

| File name                                   | Result | Error log / further info                                                                                                                |
|---------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------|
| fail-ibp002-business_logic_only.ifc         | W00030 | Alignment contains business logic only with no geometric representation                                                                 |
| fail-ibp002-representation_only.ifc         | W00030 | Alignment contains geometric representation only with no business logic                                                                 |
| pass-ibp002-same_segment_geometry_types.ifc | P00010 | All logic segments correspond to correct representation entity types, which are acquired via traversal of `IfcAlignment` representation |
