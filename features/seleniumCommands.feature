Feature: Testing all user commands
  Background:
  Given user opens automation demo page
    @checkboxes
    Scenario: checkboxes testing
      Then user selects all checkboxes and quit

    @dropdown
    Scenario: select option using dropdown
      Then user clicks dropdown and selects country using Select command
      And user quits the browser

    @datepicker
    Scenario: pick a date
      Then user selects the date

    @datepicker_dropdown
    Scenario: pick dates
      Then user opts date

    @datepicker_range
    Scenario: datepicker range
      Then user selects datepicker range