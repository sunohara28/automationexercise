from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

class Account_Created_Elements:

    header_account_created = "//b[text()='Account Created!']"
    button_continue = "a[data-qa='continue-button']"

    def __init__(self,driver):
        self.driver = driver
