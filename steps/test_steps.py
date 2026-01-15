from time import sleep

from pycparser.c_ast import Break
from pytest_bdd import parsers
from pytest_bdd import *
from selenium.webdriver import Keys

from steps.degi_data import DegiClassroomData
from steps.locators import DegiLocators

scenarios('../features/VerifyAssignScheduleToAndConfirmationFromSearchLoggedInUser.feature')

@given('Navigate to the Discovery Education')
def navigate_to_the_discovery_education(browser):
    browser.get("https://app.discoveryeducation.com/")

@when('Click on the Educator Button')
def click_on_the_educator_button(browser):
    if browser.wait_for_element_displayed(DegiLocators.user_type_teacher_card):
        browser.find_element(DegiLocators.user_type_teacher_card).click()
        browser.wait_for_element_displayed(DegiLocators.signin_username_input)


@when(parsers.parse('Login to the Education Tech with "{username}" and "{password}"'))
def login_to_the_discovery_education(browser, username, password):
      browser.wait_for_element_displayed(DegiLocators.signin_username_input)
      browser.find_element(DegiLocators.signin_username_input).send_keys(username)
      browser.wait_for_element_displayed(DegiLocators.username_continue_button)
      browser.click(DegiLocators.username_continue_button)
      browser.wait_for_element_displayed(DegiLocators.signin_password_input)
      browser.find_element(DegiLocators.signin_password_input).send_keys(password)
      browser.click(DegiLocators.singin_submit_button)
      browser.wait_for_element_displayed(DegiLocators.stay_signin_popup_no)
      browser.click(DegiLocators.stay_signin_popup_no)

@then('Verify the Educator lands on the Homepage')
def verify_the_educator_lands(browser):
    browser.wait_for_element_displayed(DegiLocators.discovery_logo_on_header)
    browser.wait_for_element_displayed(DegiLocators.discovery_logo_on_header)
    browser.wait_for_element_displayed(DegiLocators.personalized_title_homepage)

@when(parsers.parse('Click on Profile and Click on "{option}" button'))
def click_on_profile_button(browser, option):
    browser.click(DegiLocators.open_profile_panel)
    browser.wait_for_element_displayed(DegiLocators.click_profile_panel_option(option))
    browser.click(DegiLocators.click_profile_panel_option(option))

@when(parsers.parse('Click on the "{button_name}" button on the logout page'))
def click_on_the_button_on_logout_page(browser, button_name):
    if button_name == 'Sign out':
        browser.wait_for_element_displayed(DegiLocators.sign_out_completely)
        browser.click(DegiLocators.sign_out_completely)
    else:
        browser.wait_for_element_displayed(DegiLocators.back_to_home)
        browser.click(DegiLocators.back_to_home)

@then('Verify the Sign up page elements')
def verify_signup_page_elements(browser):
    browser.wait_for_element_displayed(DegiLocators.sign_up_page_label)
    browser.wait_for_element_displayed(DegiLocators.sing_up_page_links)

@when(parsers.parse('Enter the "{search_keyword}" in the search bar'))
def enter_the_search_keyword(browser, search_keyword):
    browser.wait_for_element_displayed(DegiLocators.search_input_bar)
    browser.find_element(DegiLocators.search_input_bar).send_keys(search_keyword, Keys.ENTER)

@then('Verify the user navigates to the search result page')
def verify_user_navigation_page(browser):
    browser.wait_for_element_displayed(DegiLocators.search_page_filters)
    browser.wait_for_element_displayed(DegiLocators.search_results_header_line)

@when('Scroll down to PDF Activity Card and Click on Ellipses Button and Assign Button')
def scroll_down_page_and_click_on_activity_ellipses(browser):
    browser.page_scroll_down(0, 900)
    browser.wait_for_element_displayed(DegiLocators.PDF_activity_card_ellipses)
    browser.click(DegiLocators.PDF_activity_card_ellipses)
    browser.wait_for_element_clickable(DegiLocators.PDF_activity_card_ellipses_assign_button)
    browser.click(DegiLocators.PDF_activity_card_ellipses_assign_button)

@then('Verify the Create Assignment Page')
def verify_create_assignment_page(browser):
    browser.wait_for_element_displayed(DegiLocators.create_assignment_heading)
    browser.wait_for_element_displayed(DegiLocators.choose_how_to_assign_text)
    browser.wait_for_element_displayed(DegiLocators.assign_to_your_student_button)

@when('Click on assign to classroom select student and click on next button')
def click_assignto_classroom_checkbox_next_button(browser):
    browser.click(DegiLocators.assign_to_your_student_button)
    browser.wait_for_element_displayed(DegiLocators.classroom_checkbox_on_assignTo)
    browser.click(DegiLocators.classroom_checkbox_on_assignTo)
    browser.click(DegiLocators.classroom_select_student_buttons)
    browser.wait_for_element_displayed(DegiLocators.assign_section_next_button)
    browser.click(DegiLocators.assign_section_next_button)

@when('Set start and due date and click on Assign button')
def set_start_and_due_date_assign(browser):
    browser.wait_for_element_displayed(DegiLocators.Schedule_title_on_date_page)

    browser.click(DegiLocators.start_date_calender)
    browser.wait_for_element_displayed(DegiLocators.select_date_button)
    browser.not_visible_click(DegiLocators.select_date)
    browser.not_visible_click(DegiLocators.select_date_button)

    browser.wait_for_element_displayed(DegiLocators.due_date_calender)
    browser.click(DegiLocators.due_date_calender)
    browser.wait_for_element_displayed(DegiLocators.select_date_button)
    browser.not_visible_click(DegiLocators.select_date)
    browser.click(DegiLocators.select_date_button)

    browser.wait_for_element_displayed(DegiLocators.schedule_assign_button)
    browser.click(DegiLocators.schedule_assign_button)

@then('Verify Assignment Confirmation Page')
def verify_assignment_confirmation_page(browser):
    browser.wait_for_element_displayed(DegiLocators.confirmation_final_steps)
    browser.verify_text_within_text_on_page(DegiLocators.confirmation_title, DegiClassroomData.assignment_confirmation_page[0])
    browser.verify_text_within_text_on_page(DegiLocators.successfully_assign_to, DegiClassroomData.assignment_confirmation_page[1])
    browser.wait_for_element_displayed(DegiLocators.view_all_assignments_button)

@when('Click on the view all assignment button')
def click_all_assignment_button(browser):
    browser.wait_for_element_displayed(DegiLocators.view_all_assignments_button)
    browser.click(DegiLocators.view_all_assignments_button)

@then('Verify the assignment name and Assignment manager page')
def verify_assignment_on_assignment_page(browser):
    browser.wait_for_element_displayed(DegiLocators.assignment_manager_title)
    browser.wait_for_element_displayed(DegiLocators.assignment_name_on_table)

@when('Unassign the existing assignment in the Assignment manager')
def unassign_assignment_in_assignment_manager_page(browser):
    browser.wait_for_element_displayed(DegiLocators.global_navigation_hamburger_menu)
    browser.click(DegiLocators.global_navigation_hamburger_menu)
    browser.wait_for_element_displayed(DegiLocators.assignment_manager_button)
    browser.click(DegiLocators.assignment_manager_button)
    browser.wait_for_element_displayed(DegiLocators.assignment_manager_title)
    if browser.wait_for_element_displayed(DegiLocators.ellipses_button):
         while True:
            if browser.wait_for_element_displayed(DegiLocators.ellipses_button):
                browser.wait_for_element_displayed(DegiLocators.ellipses_button)
                browser.click(DegiLocators.ellipses_button)
                browser.click(DegiLocators.unassign_button)
                browser.wait_for_element_displayed(DegiLocators.unassign_button_on_popup)
                browser.click(DegiLocators.unassign_button_on_popup)
    else:
        browser.click(DegiLocators.discovery_logo_on_header)






