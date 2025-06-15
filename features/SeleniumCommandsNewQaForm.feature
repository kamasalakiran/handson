Feature: all commands testing
  Background:
    Given new qa form is opened
    @check_boxes
    Scenario: checkboxes using button
      Then user selects checkboxes
      Then user performs operations on buttons
      And user download a file and save it his preferred location
      And user upload a file

    @dynamic_buttons
    Scenario: user plays with dynamic buttons
      Then user plays with dynamic buttons

    @alerts
    Scenario: user plays with alerts
      Then user plays with alerts

    @frames_sliders
    Scenario: user plays with frames
      Then user plays with frame
      And user plays with nested frames
      And user plays with slider
      Then user plays with progress bar

    @scrolling
    Scenario: user plays with scrolling
      Then user plays with scroll button

    @drag_and_drop
    Scenario: user plays with drag and drop
      Then user plays with drag and drop
      Then user plays with revert
      And user plays with selectable
      Then user plays resizable

    @tables
    Scenario: user plays with tables
      Then user plays with tables

    @brokenLinks
    Scenario: user plays with broken links
      Then user plays with broken links




