from csv import excel

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


DEFAULT_TIMEOUT = 30
LONG_DEFAULT_TIMEOUT = 60
SHORT_DEFAULT_TIMEOUT = 15
TWO_SECOND_TIMEOUT = 2


class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def get(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        by, value = locator
        return self.driver.find_element(by, value)

    def find_elements(self, locator):
        by, value = locator
        return self.driver.find_elements(by, value)

    def click(self, locator):
        by, value = locator
        self.driver.find_element(by, value).click()

    def type(self, locator, value):
        self.wait_for_element_displayed(locator)
        element = self.driver.find_element(locator)
        element.send_keys(value)

    def wait_for_element_displayed(self, locator):
        by, value = locator
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.visibility_of_element_located((by, value)))

    def wait_for_element_clickable(self, locator):
        by, value = locator
        return WebDriverWait(self.driver, TWO_SECOND_TIMEOUT).until(EC.element_to_be_clickable((by, value)))

    def quit(self):
        self.driver.quit()

    def switch_to_new_window(self):
        new_window_position = len(self.driver.window_handles) -1
        new_window = self.driver.window_handles[new_window_position]
        self.driver.switch_to.window(new_window)

    def switch_back_to_first_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    def page_scroll_down(self, xaxis, yaxis):
        command = "window.scrollBy({}, {})".format(xaxis, yaxis)
        self.driver.execute_script(command)

    def mouse_hover_click(self, locator):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(locator)
        actions.move_to_element(element).click().perform()

    def click_back_button(self):
        return self.driver.back()

    def not_visible_click(self, locator):
        by, value = locator
        ele = self.driver.find_element(by, value)
        self.driver.execute_script("arguments[0].click();", ele)

    def verify_text_within_text_on_page(self, locator, text):
        self.wait_for_element_displayed(locator)
        text_found = self.find_element(locator).text
        if text in text_found:
            return True
        return None


