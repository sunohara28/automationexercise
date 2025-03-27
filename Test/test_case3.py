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

    def test_login(self):
        userAccountData = csvReader.csvReader(csvReader.accountData)
        Signup_Loc = Signup_Login_Locators(self.driver)

        try:
            assert (Signup_Loc.header_locator(Signup_Login_Locators.header_login).is_displayed()
                    and Signup_Loc.header_locator(Signup_Login_Locators.header_login).text == "Login to your account")
        except NoSuchElementException as triggeredException:
            print("Header login is not displayed", triggeredException)

        Signup_Loc.login_signup_account(Signup_Login_Locators.field_login_email,userAccountData[0]['email'],
                  Signup_Login_Locators.field_login_pass,userAccountData[0]['password'])

        Signup_Loc.submit(Signup_Loc.button_login)

    def test_verify_incorrect_creds(self):
        Signup_Loc = Signup_Login_Locators(self.driver)

        try:
            assert Signup_Loc.error_message(Signup_Loc.error_incorrect_credentials).is_displayed()
        except NoSuchElementException as triggeredException:
            print("error message did not displayed",triggeredException)
