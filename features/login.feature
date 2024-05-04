Feature: Login Feature
    As a user
    I want to be able to log in to my account
    So that I can access my dashboard

Scenario: Successful Login
    Given I am on the login page
    When I enter my email and password
    And I click on the Sign In button
    Then I should be logged in successfully
