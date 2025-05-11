from Objects.General_Locator import General_Locators
from Test.WebDriver import InitDriver
from Objects.Menu import Menu_Elements
from Objects.Test_cases import TestCase_Elements
from selenium.common import NoSuchElementException

class TestMain(InitDriver):
    def test_homepage(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_test_case)
        General_Loc.element_locator_css(Menu_Elements.link_test_case).click()

    def test_testcase(self):
        General_Loc = General_Locators(self.driver)

        try:
            assert General_Loc.element_locator_xpath(TestCase_Elements.header_testcase).is_displayed()
        except NoSuchElementException as triggeredException:
            print("Test Case header is not displayed",triggeredException)


