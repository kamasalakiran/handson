Feature: Login into a page and taking screenshot
  Scenario: Login and taking a Screenshot
    Given the login page is open
    When user enter username and password
    And user clicks on login button
    Then homepage should be opened and user verifies title
    And takes screenshot

  @EC_Commands
  Scenario: practicing Wait Commands
    Given the Orangehrm page is open
    Then I wait for username and password locators to be present
    And user open another website
    Then user selects male option
    Then user verifies element visibility, text presence and radio buttons selection
    And User closes the browser

  @DataDrivenTesting
  Scenario Outline: multiple entries of username and passwords
    When user opens login page
    When user enters "<username>" and "<password>"
    And user clicks on submit button
    Then Homepage opens and title gets verified
    And  screenshot taken

    Examples:
      | username        | password      |
      | standard_user   | secret_sauce  |
      | problem_user    | secret_sauce  |
      | error_user      | secret_sauce  |
      | visual_user     | secret_sauce  |
