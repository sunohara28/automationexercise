from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

class TestCase_Locators:

    header_testcase = "//b[text()='Test Cases']"

    def __init__(self,driver):
        self.driver = driver

    def wait_element_XPATH(self,element):
        return WebDriverWait(self.driver, 5).until(presence_of_element_located((By.XPATH, element)))

    def header_locator(self,element):
        return self.driver.find_element(By.XPATH, element)

