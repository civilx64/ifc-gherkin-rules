| File name                                    | Expected result   | Error                                                                                                                                  | Description   |
|:---------------------------------------------|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------|:--------------|
| pass-gem005-aggregate.ifc                    | pass              | Rules passed                                                                                                                           |               |
| fail-gem005-scenario01-no_representation.ifc | fail              | ['On instance None the following invalid value for RepresentationIdentifier has been found: Attribute not found']                      |               |
| pass-gem005-contain.ifc                      | pass              | Rules passed                                                                                                                           |               |
| fail-gem005-scenario01-footprint.ifc         | fail              | ['On instance #30=IfcShapeRepresentatio...,(#29)) the following invalid value for RepresentationIdentifier has been found: FootPrint'] |               |
| pass-gem005-body.ifc                         | pass              | Rules passed                                                                                                                           |               |