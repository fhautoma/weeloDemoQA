#@use.Windows.10.Chrome.95.browserstack
@use.chrome.browser

Feature: Fill Student Registration Form
  the purpose of this test is to register new student in Demo_QA page


  Background: have at least browser installed

  Scenario: Create Student in Demo_QA page
    Given a browser is used to load the URL "https://demoqa.com/automation-practice-form"
    When I fill student registration form
    And I click submit button
    Then I see a table with new student information