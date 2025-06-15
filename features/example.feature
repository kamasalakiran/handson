Feature: Feature Practice
  Background:
    Given the login page is opened
  Scenario Outline: practicing Scenario outline
    Given the one uses "<username>" and "<password>"
    Then the two and "<age>"
    Then habibi

    Examples:
    | username | password | age|
    | kiran    | 1234     |  2 |
    | sudhu    | 123      | 55 |
    | orang    | 456      | 67 |



