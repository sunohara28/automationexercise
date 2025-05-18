from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

class TestCase_Elements:

    header_testcase = "//b[text()='Test Cases']"

class TestCase_Locators:

    def __init__(self,driver):
        self.driver = driver

