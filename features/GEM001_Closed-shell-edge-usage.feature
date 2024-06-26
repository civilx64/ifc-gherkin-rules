@informal-proposition
@GEM
@version1
@E00050
Feature: GEM001 - Closed shell edge usage
The rule verifies that closed shells and closed facesets edges are referenced correctly.

  Scenario: IfcClosedShell

    Given An IfcClosedShell

    Then Every edge must be referenced exactly 2 times by the loops of the face
    Then Every oriented edge must be referenced exactly 1 times by the loops of the face
  

  Scenario: IfcTriangulatedFaceSet

    Given An IfcTriangulatedFaceSet
    Given Closed = True

    Then Every edge must be referenced exactly 2 times by the loops of the face
    Then Every oriented edge must be referenced exactly 1 times by the loops of the face


  Scenario: IfcPolygonalFaceSet

    Given An IfcPolygonalFaceSet
    Given Closed = True

    Then Every edge must be referenced exactly 2 times by the loops of the face
    Then Every oriented edge must be referenced exactly 1 times by the loops of the face
