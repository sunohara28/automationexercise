from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Signup_Login_Elements:

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

class Signup_Login_Locators:

    def __init__(self,driver):
        self.driver = driver

    def login_account(self,email,password):
        self.driver.find_element(By.CSS_SELECTOR, Signup_Login_Elements.field_login_email).send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, Signup_Login_Elements.field_login_pass).send_keys(password)

    def signup_account(self,name,email):
        self.driver.find_element(By.CSS_SELECTOR, Signup_Login_Elements.field_signup_name).send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, Signup_Login_Elements.field_signup_email).send_keys(email)




    