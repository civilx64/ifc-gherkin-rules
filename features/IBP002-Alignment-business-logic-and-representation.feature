@IBP
@industry-practice
@version1
@W00030

Feature: IBP002 - Alignment business logic and representation

The rule verifies that alignments contain both business logic and representation.
This is considered a best practice as it provides the full breadth of information for kinematic considerations
as well as geometric visualization and analysis.

Scenario: Agreement on IfcAlignment containing both business logic and representation

    Given An IfcAlignment
    Then It should contain both business logic and representation
