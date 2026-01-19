Feature: Login to Education Tech
  Background:
    Given Navigate to the Education Tech
    When Click on the Educator Button

Scenario: Login to the Ed-Tech Web App as Trainer

#@@when(parsers.parse('Login to the Education Tech with "{username}" and "{password}"'))
  When Login to the Education Tech with "username" and "password"
  Then Verify the Educator lands on the Homepage
#@when(parsers.parse('Click on Profile and Click on "{option}" button'))
  When Click on Profile and Click on "Sign Out" button
#@when(parsers.parse('Click on the "{option}" button on the logout page'))
  And  Click on the "Sign out" button on the logout page
  Then Verify the Sign up page elements