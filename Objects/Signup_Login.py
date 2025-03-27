from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class Signup_Login_Locators:

    header_login = "div[class='login-form'] h2"
    header_signup = "div[class='signup-form'] h2"
    field_signup_name = "input[data-qa='signup-name']"
    field_signup_email = "input[data-qa='signup-email']"
    field_login_email ="input[data-qa='login-email']"
    field_login_pass = "input[data-qa='login-password']"
    button_login = "button[data-qa='login-button']"
    button_signup = "button[data-qa='signup-button']"

    error_email_already_exist = "//p[text()='Email Address already exist!']"
    error_incorrect_credentials = "//p[text()='Your email or password is incorrect!']"

    def __init__(self,driver):
        self.driver = driver

    def wait_element(self,element):
        return WebDriverWait(self.driver,5).until(presence_of_element_located((By.CSS_SELECTOR,element)))

    def wait_error_element(self,element):
        return WebDriverWait(self.driver,5).until(presence_of_element_located((By.XPATH,element)))
    
    def header_locator(self,header):
        return self.driver.find_element(By.CSS_SELECTOR, header)

    def error_message(self,error_message):
        return self.driver.find_element(By.XPATH,error_message)

    def login_signup_account(self, field1,value1,field2,value2):

        account_info_fields = [(field1, value1),
                               (field2, value2)]

        for field, value in account_info_fields:
            self.driver.find_element(By.CSS_SELECTOR, field).send_keys(value)

    def submit(self,button):
        return self.driver.find_element(By.CSS_SELECTOR,button).click()



    