@informal-proposition
@SWE
@version1
Feature: SWE003 - Number of points and edges for IfcSectionedSolidHorizontal profiles

The rule verifies that if the type of sections is not IfcParameterizedProfileDef,
then the number of points and edges must be the same for two consecutive profiles.
The rule only verifies profiles of type IfcArbitraryClosedProfileDef.

  Background: Sections for IfcSectionedSolidHorizontal

    Given a model with Schema 'IFC4.3'

    Given an .IfcSectionedSolidHorizontal.

  Scenario: Same number of edges

    Given the [edges] of .CrossSections.
    Given the number of [edges]
    Then the values must be identical at depth 1

  Scenario: Same number of points

    Given the [points] of .CrossSections.
    Given the number of [points]
    Then the values must be identical at depth 1

