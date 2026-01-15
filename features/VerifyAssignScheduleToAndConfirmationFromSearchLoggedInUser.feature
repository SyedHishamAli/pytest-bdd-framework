Feature: Verify Assign Schedule To And Confirmation From Search Teacher Login

  Background:
    Given Navigate to the Discovery Education
    When Click on the Educator Button

 @test
Scenario: Verify Assign Schedule To And Confirmation From Search
    When Login to the Education Tech with "AT_Degi_Teacher13" and "disc0verme"
    Then Verify the Educator lands on the Homepage
    When Unassign the existing assignment in the Assignment manager
    When Enter the "Science Techbook" in the search bar
    Then Verify the user navigates to the search result page
    When Scroll down to PDF Activity Card and Click on Ellipses Button and Assign Button
    Then Verify the Create Assignment Page
    When Click on next button
    And  Set start and due date and click on Assign button
    Then Verify Assignment Confirmation Page
    When Click on the view all assignment button
    Then Verify the assignment name and Assignment manager page
    When Click on Profile and Click on "Sign Out" button
    #@when(parsers.parse('Click on the "{option}" button on the logout page'))
    And  Click on the "Sign out" button on the logout page
    Then Verify the Sign up page elements
