import pytest
from selenium.common import NoSuchElementException
import Test.csv_Reader as csvReader
from Test.WebDriver import InitDriver
from Objects.Menu import Menu_Locators, Menu_Elements
from Objects.General_Locator import General_Locators
from Objects.Signup_Login import Signup_Login_Locators , Signup_Login_Elements
from Objects.Signup_acc_info import Signup_acc_Locators, Signup_acc_Elements
from Objects.Account_created import Account_Created_Elements
from Objects.Account_deleted import Account_Deleted_Elements


class TestMain(InitDriver):

    def test_navigate_to_signup(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_signup_login)
        General_Loc.element_locator_css(Menu_Elements.link_signup_login).click()

    def test_signup(self):
        userAccountData = csvReader.csvReader(csvReader.accountData)
        General_Loc = General_Locators(self.driver)
        Signup_Loc = Signup_Login_Locators(self.driver)

        General_Loc.multiple_wait_element_css(
                Signup_Login_Elements.header_signup,
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

    def test_account_info(self):
        userAccountData = csvReader.csvReader(csvReader.accountData)
        General_Loc = General_Locators(self.driver)
        Signup_acc_Loc = Signup_acc_Locators(self.driver)

        General_Loc.multiple_wait_element_css(Signup_acc_Elements.button_create_account)

        try:
            assert (General_Loc.element_locator_xpath(Signup_acc_Elements.header_account_info).is_displayed()
                    and
                    General_Loc.element_locator_xpath(Signup_acc_Elements.header_account_info).is_displayed())
        except NoSuchElementException as triggeredException:
            print("Header account info is not displayed", triggeredException)

        Signup_acc_Loc.fill_signup_account_info(userAccountData[0]['gender'],
                                                userAccountData[0]['password'],
                                                userAccountData[0]['days'],
                                                userAccountData[0]['months'],
                                                userAccountData[0]['years'],
                                                userAccountData[0]['newsletter'],
                                                userAccountData[0]['optin'])
        Signup_acc_Loc.fill_signup_account_addr_info(userAccountData[0]['first_name'],
                                                     userAccountData[0]['last_name'],
                                                     userAccountData[0]['company'],
                                                     userAccountData[0]['addr1'],
                                                     userAccountData[0]['addr2'],
                                                     userAccountData[0]['state'],
                                                     userAccountData[0]['city'],
                                                     userAccountData[0]['zipcode'],
                                                     userAccountData[0]['mobile_number'])

        Signup_acc_Loc.select_cntry(userAccountData[0]['country'])

        General_Loc.element_locator_css(Signup_acc_Elements.button_create_account).click()

    def test_verify_acc_created(self):
        General_Loc = General_Locators(self.driver)

        try:
            assert General_Loc.element_locator_xpath(Account_Created_Elements.header_account_created).is_displayed()
        except NoSuchElementException as triggeredException:
            print("header account created is not displayed", triggeredException)

        General_Loc.wait_element_css(Account_Created_Elements.button_continue)
        General_Loc.element_locator_css(Account_Created_Elements.button_continue).click()

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

        General_Loc.element_locator_css(Menu_Elements.link_delete_account).click()

    def test_verify_acc_del(self):
        General_Loc = General_Locators(self.driver)

        assert General_Loc.element_locator_xpath(Account_Deleted_Elements.header_account_deleted).is_displayed()

        General_Loc.element_locator_css(Account_Deleted_Elements.button_continue).click()



        

