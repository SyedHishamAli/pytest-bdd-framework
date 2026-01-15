Feature: Login to the Discovery Education
  Background:
    Given Navigate to the Discovery Education
    When Click on the Educator Button

Scenario: Login to the Discovery Education as a Teacher

#@@when(parsers.parse('Login to the Discovery Education with "{username}" and "{password}"'))
  When Login to the Discovery Education with "AT_Degi_Teacher13" and "disc0verme"
  Then Verify the Educator lands on the Homepage
#@when(parsers.parse('Click on Profile and Click on "{option}" button'))
  When Click on Profile and Click on "Sign Out" button
#@when(parsers.parse('Click on the "{option}" button on the logout page'))
  And  Click on the "Sign out" button on the logout page
  Then Verify the Sign up page elements