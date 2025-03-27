import pytest
from selenium.common import NoSuchElementException
import Test.csv_Reader as csvReader
from Test.WebDriver import InitDriver
from Objects.Menu import Menu_Locators
from Objects.Signup_Login import Signup_Login_Locators
from Objects.Signup_acc_info import Signup_acc_Locators
from Objects.Account_created import Account_Created_Locators
from Objects.Account_deleted import Account_Deleted_Locators

class TestMain(InitDriver):
    def test_homepage(self):
        Menu_Loc = Menu_Locators(self.driver)

        assert Menu_Loc.link_locator(Menu_Loc.link_signup_login).is_displayed()
        Menu_Loc.link_locator(Menu_Loc.link_signup_login).click()

    def test_signup(self):
        userAccountData = csvReader.csvReader(csvReader.accountData)
        Signup_Loc = Signup_Login_Locators(self.driver)

        try:
            assert Signup_Loc.header_locator(
                Signup_Loc.header_signup).is_displayed() and Signup_Loc.header_locator(
                Signup_Loc.header_signup).text == "New User Signup!"
        except NoSuchElementException as triggeredException:
            print("Header signup is not displayed", triggeredException)

        Signup_Loc.login_signup_account(Signup_Loc.field_signup_name,userAccountData[0]['name'],Signup_Loc.field_signup_email,userAccountData[0]['email'])

        Signup_Loc.submit(Signup_Loc.button_signup)

    def test_error_message(self):
        Signup_Loc = Signup_Login_Locators(self.driver)

        Signup_Loc.wait_error_element(Signup_Loc.error_email_already_exist)

        try:
            assert Signup_Loc.error_message(Signup_Loc.error_email_already_exist).is_displayed()
        except NoSuchElementException as triggeredException:
            print("error message did not displayed", triggeredException)
