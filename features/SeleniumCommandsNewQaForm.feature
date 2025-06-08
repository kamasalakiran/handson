Feature: all commands testing
  Background:
    Given new qa form is opened
    @check_boxes
    Scenario: checkboxes using button
      Then user selects checkboxes
      Then user performs operations on buttons
      And user download a file and save it his preferred location