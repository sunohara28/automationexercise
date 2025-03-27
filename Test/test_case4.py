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

        Menu_Loc.wait_element(Menu_Loc.link_signup_login)
        assert Menu_Loc.link_locator(Menu_Loc.link_signup_login).is_displayed()
        Menu_Loc.link_locator(Menu_Loc.link_signup_login).click()

    def test_login(self):
        userAccountData = csvReader.csvReader(csvReader.accountData)
        Signup_Login_Loc = Signup_Login_Locators(self.driver)

        try:
            assert (Signup_Login_Loc.header_locator(Signup_Login_Locators.header_login).is_displayed()
                    and Signup_Login_Loc.header_locator(Signup_Login_Locators.header_login).text == "Login to your account")
        except NoSuchElementException as triggeredException:
            print("Header login is not displayed", triggeredException)

        Signup_Login_Loc.login_signup_account(Signup_Login_Locators.field_login_email,userAccountData[0]['email'],
                  Signup_Login_Locators.field_login_pass,userAccountData[0]['password'])

        Signup_Login_Loc.submit(Signup_Login_Loc.button_login)

    def test_verify_logged_in(self):
        userAccountData = csvReader.csvReader(csvReader.accountData)
        Menu_Loc = Menu_Locators(self.driver)

        try:
            assert Menu_Loc.logged_in().is_displayed()
            assert Menu_Loc.logged_in_user(userAccountData[0]['name']).is_displayed()
        except NoSuchElementException as triggeredException:
            print("Logged in displayed error ",triggeredException)

    def test_logout(self):
        Menu_Loc = Menu_Locators(self.driver)

        Menu_Loc.link_locator(Menu_Loc.link_logout).click()

    def test_verify_logout(self):
        Signup_Login_Loc = Signup_Login_Locators(self.driver)

        Signup_Login_Loc.wait_element(Signup_Login_Loc.header_login)

        try:
            assert (Signup_Login_Loc.header_locator(Signup_Login_Locators.header_login).is_displayed()
                    and Signup_Login_Loc.header_locator(Signup_Login_Locators.header_login).text == "Login to your account")
        except NoSuchElementException as triggeredException:
            print("Header login is not displayed", triggeredException)
