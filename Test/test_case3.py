import pytest
from selenium.common import NoSuchElementException
import Test.csv_Reader as csvReader
from Objects.General_Locator import General_Locators
from Test.WebDriver import InitDriver
from Objects.Menu import Menu_Elements
from Objects.Signup_Login import Signup_Login_Locators, Signup_Login_Elements

class TestMain(InitDriver):
    def test_test_navigate_to_login(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_signup_login)
        General_Loc.element_locator_css(Menu_Elements.link_signup_login).click()

    def test_login(self):
        userAccountData = csvReader.csvReader(csvReader.accountData)
        Signup_Loc = Signup_Login_Locators(self.driver)
        General_Loc = General_Locators(self.driver)

        General_Loc.multiple_wait_element_css(Signup_Login_Elements.field_login_email,
                                              Signup_Login_Elements.field_login_pass,
                                              Signup_Login_Elements.button_login)

        try:
            assert (General_Loc.element_locator_css(Signup_Login_Elements.header_login).is_displayed()
                    and General_Loc.element_locator_css(Signup_Login_Elements.header_login).text == "Login to your account")
        except NoSuchElementException as triggeredException:
            print("Header login is not displayed", triggeredException)

        Signup_Loc.login_account(userAccountData[0]['email'],userAccountData[0]['password'])

        General_Loc.element_locator_css(Signup_Login_Elements.button_login).click()

    def test_verify_incorrect_creds(self):
        General_Loc = General_Locators(self.driver)

        try:
            assert General_Loc.element_locator_xpath(Signup_Login_Elements.error_incorrect_credentials).is_displayed()
        except NoSuchElementException as triggeredException:
            print("error message did not displayed",triggeredException)
