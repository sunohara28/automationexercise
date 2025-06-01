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
from Utils.Screenshot import Screenshot


class TestMain(InitDriver):

    def test_navigate_to_signup(self):
        General_Loc = General_Locators(self.driver)
        ss = Screenshot(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_signup_login)
        General_Loc.element_locator_css(Menu_Elements.link_signup_login).click()
