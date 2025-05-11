from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class Account_Deleted_Elements:

    header_account_deleted = "//b[text()='Account Deleted!']"
    button_continue = "a[data-qa='continue-button']"

class Account_Deleted_Locators:

    def __init__(self,driver):
        self.driver = driver

