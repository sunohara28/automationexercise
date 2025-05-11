import pytest
from selenium.common import NoSuchElementException
import Test.csv_Reader as csvReader
from Test.WebDriver import InitDriver
from Objects.Menu import Menu_Elements, Menu_Locators
from Objects.General_Locator import General_Locators
from Objects.Signup_Login import Signup_Login_Locators,Signup_Login_Elements
from Objects.Account_deleted import Account_Deleted_Elements


class TestMain(InitDriver):
    def test_navigate_to_login(self):
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

    def test_verify_logged_in(self):
        userAccountData = csvReader.csvReader(csvReader.accountData)
        General_Loc = General_Locators(self.driver)
        Menu_Loc = Menu_Locators(self.driver)

        try:
            assert General_Loc.element_locator_xpath(Menu_Elements.logged_in_locator).is_displayed()
            assert Menu_Loc.logged_in_user(userAccountData[0]['name']).is_displayed()
        except NoSuchElementException as triggeredException:
            print("Logged in displayed error ",triggeredException)

    def test_delete_account(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_delete_account)
        General_Loc.element_locator_css(Menu_Elements.link_delete_account).click()

    def test_verify_acc_del(self):
        General_Loc = General_Locators(self.driver)

        assert General_Loc.wait_element_xpath(Account_Deleted_Elements.button_continue).is_displayed()

        General_Loc.wait_element_css(Account_Deleted_Elements.button_continue)
        General_Loc.element_locator_css(Account_Deleted_Elements.button_continue).click()