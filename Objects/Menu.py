from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Menu_Locators:

    link_home = "a[href='/']"
    link_products = "a[href='/products']"
    link_cart = "a[href='/view_cart']"
    link_signup_login = "a[href='/login']"
    link_logout = "a[href='/logout']"
    link_delete_account = "a[href='/delete']"
    link_contact_us = "a[href='/contact_us']"
    link_test_case = "a[href='/test_case']"
    
    logged_in_locator = "//li[contains(.,'Logged in')]"


    def __init__(self,driver):
        self.driver = driver

    def wait_element_css(self,element):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))

    def link_locator(self,element):
        Menu_Locators.wait_element_css(self, element)
        return self.driver.find_element(By.CSS_SELECTOR,element)

    def logged_in(self):
        return self.driver.find_element(By.XPATH, Menu_Locators.logged_in_locator)

    def logged_in_user(self,name):
        return self.driver.find_element(By.XPATH,f"//li/a/b[contains(.,'{name}')]")