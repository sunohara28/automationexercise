import asyncio

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
    async def test_homepage(self):
        Menu_Loc = Menu_Locators(self.driver)

        await Menu_Loc.link_locator(Menu_Loc.link_signup_login).click()


    async def test_signup(self):
        userAccountData = csvReader.csvReader(csvReader.accountData)
        Signup_Loc = Signup_Login_Locators(self.driver)

        try:
            assert Signup_Loc.header_locator(
                Signup_Loc.header_signup).is_displayed() and Signup_Loc.header_locator(
                Signup_Loc.header_signup).text == "New User Signup!"
        except NoSuchElementException as triggeredException:
            print("Header signup is not displayed", triggeredException)

        Signup_Loc.login_signup_account(Signup_Loc.field_signup_name,userAccountData[0]['name'],Signup_Loc.field_signup_email,userAccountData[0]['email'])

        await Signup_Loc.submit(Signup_Loc.button_signup)

    @pytest.mark.skip
    def test_account_info(self):
        userAccountData = csvReader.csvReader(csvReader.accountData)
        Signup_acc_Loc = Signup_acc_Locators(self.driver)

        try:
            assert Signup_acc_Loc.header_signup_locator(Signup_acc_Loc.header_account_info).is_displayed() and Signup_acc_Loc.header_signup_locator(Signup_acc_Loc.header_account_info).is_displayed()
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

        Signup_acc_Loc.submit_create_account()

    @pytest.mark.skip
    def test_verify_acc_created(self):
        Account_Created_Loc = Account_Created_Locators(self.driver)

        try:
            assert Account_Created_Loc.header_account_created_locator().is_displayed()
        except NoSuchElementException as triggeredException:
            print("header account created is not displayed", triggeredException)

        Account_Created_Loc.click_continue()

    @pytest.mark.skip
    def test_verify_logged_in(self):
        userAccountData = csvReader.csvReader(csvReader.accountData)
        Menu_Loc = Menu_Locators(self.driver)

        try:
            assert Menu_Loc.logged_in().is_displayed()
            assert Menu_Loc.logged_in_user(userAccountData[0]['name']).is_displayed()
        except NoSuchElementException as triggeredException:
            print("Logged in displayed error ",triggeredException)

    @pytest.mark.skip
    def test_delete_account(self):
        Menu_Loc = Menu_Locators(self.driver)

        Menu_Loc.link_locator(Menu_Loc.link_delete_account).click()

    @pytest.mark.skip
    def test_verify_acc_del(self):
        Account_Deleted_Loc = Account_Deleted_Locators(self.driver)

        assert Account_Deleted_Loc.header_account_deleted_locator().is_displayed()

        Account_Deleted_Loc.click_continue()




        

