from Test.WebDriver import InitDriver
from Objects.Menu import Menu_Locators
from Objects.TestCases import TestCase_Locators
from selenium.common import NoSuchElementException

class TestMain(InitDriver):
    def test_homepage(self):
        Menu_Loc = Menu_Locators(self.driver)

        assert Menu_Loc.link_locator(Menu_Loc.link_test_case).is_displayed()
        Menu_Loc.link_locator(Menu_Loc.link_test_case).click()

    def test_testcase(self):
        TestCase_Loc = TestCase_Locators(self.driver)

        TestCase_Loc.wait_element_XPATH(TestCase_Loc.header_testcase)

        try:
            assert TestCase_Loc.header_locator(TestCase_Loc.header_testcase).is_displayed()
        except NoSuchElementException as triggeredException:
            print("Test Case header is not displayed",triggeredException)


