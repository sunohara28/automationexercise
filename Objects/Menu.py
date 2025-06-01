from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Menu_Elements:
    link_home = "a[href='/']"
    link_products = "a[href='/products']"
    link_cart = "a[href='/view_cart']"
    link_signup_login = "a[href='/login']"
    link_logout = "a[href='/logout']"
    link_delete_account = "a[href='/delete_account']"
    link_contact_us = "a[href='/contact_us']"
    link_test_case = "a[href='/test_cases']"
    link_api_testing = "a[href='/api_list']"

    logged_in_locator = "//li[contains(.,'Logged in')]"

class Menu_Locators:

    def __init__(self,driver):
        self.driver = driver

    def logged_in_user(self,name):
        return self.driver.find_element(By.XPATH,f"//li/a/b[contains(.,'{name}')]")