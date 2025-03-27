from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

class Account_Deleted_Locators:

    header_account_deleted = "//b[text()='Account Deleted!']"
    button_continue = "a[data-qa='continue-button']"

    def __init__(self,driver):
        self.driver = driver

    def wait_header(self):
        return WebDriverWait(self.driver,2).until(presence_of_element_located(By.XPATH,Account_Deleted_Locators.header_account_deleted))

    def header_account_deleted_locator(self):
        return self.driver.find_element(By.XPATH,Account_Deleted_Locators.header_account_deleted)
    
    def click_continue(self):
        return self.driver.find_element(By.CSS_SELECTOR,Account_Deleted_Locators.button_continue).click()


