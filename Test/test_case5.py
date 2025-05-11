import pytest
from selenium.common import NoSuchElementException
import Test.csv_Reader as csvReader
from Objects.General_Locator import General_Locators
from Test.WebDriver import InitDriver
from Objects.Menu import Menu_Elements
from Objects.Signup_Login import Signup_Login_Locators, Signup_Login_Elements

class TestMain(InitDriver):
    def test_homepage(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_signup_login)
        General_Loc.element_locator_css(Menu_Elements.link_signup_login).click()

    def test_signup(self):
        userAccountData = csvReader.csvReader(csvReader.accountData)
        General_Loc = General_Locators(self.driver)
        Signup_Loc = Signup_Login_Locators(self.driver)

        General_Loc.multiple_wait_element_css(
                         Signup_Login_Elements.field_signup_name,
                         Signup_Login_Elements.field_signup_email,
                         Signup_Login_Elements.button_signup)

        try:
            assert (General_Loc.element_locator_css(Signup_Login_Elements.header_signup).is_displayed()
                    and
                    General_Loc.element_locator_css(Signup_Login_Elements.header_signup).text == "New User Signup!")
        except NoSuchElementException as triggeredException:
            print("Header signup is not displayed", triggeredException)

        Signup_Loc.signup_account(userAccountData[0]['name'],
                                        userAccountData[0]['email'])

        General_Loc.element_locator_css(Signup_Login_Elements.button_signup).click()

    def test_error_message(self):
        General_Loc = General_Locators(self.driver)

        try:
            assert General_Loc.element_locator_xpath(Signup_Login_Elements.error_email_already_exist).is_displayed()
        except NoSuchElementException as triggeredException:
            print("error message did not displayed", triggeredException)
