from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

class Menu_Locators:

    link_home = "Home"
    link_products = "Products"
    link_card = "Cart"
    link_signup_login = "Signup / Login"
    link_logout = "Logout"
    link_delete_account = "Delete Account"
    link_contact_us = "Contact us"
    link_test_case = "Test Cases"
    
    logged_in_locator = "//li[contains(.,'Logged in')]"


    def __init__(self,driver):
        self.driver = driver

    def wait_element(self,element):
        return WebDriverWait(self.driver, 5).until(presence_of_element_located((By.LINK_TEXT, element)))

    def link_locator(self,link):
        return self.driver.find_element(By.LINK_TEXT,link)

    def logged_in(self):
        return self.driver.find_element(By.XPATH, Menu_Locators.logged_in_locator)

    def logged_in_user(self,name):
        return self.driver.find_element(By.XPATH,f"//li/a/b[contains(.,'{name}')]")