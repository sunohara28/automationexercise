import time
import Test.csv_Reader as csvReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert

class ContactUs_Locators:

    field_name = "input[name='name']"
    field_email = "input[name='email']"
    field_subject = "input[name='subject']"
    field_message = "textarea[name='message']"
    field_file = "input[name='upload_file']"

    alert_success = ".status.alert.alert-success"
    alert_home_button = ".btn.btn-success"

    button_submit = "input[name='submit']"

    header_get_in_touch = "//h2[text()='Get In Touch']"

    def __init__(self,driver):
        self.driver = driver



    def wait_field_element_CSS(self,element):
        return WebDriverWait(self.driver, 5).until(presence_of_element_located((By.CSS_SELECTOR,element)))

    def wait_header_element_XPATH(self,element):
        return WebDriverWait(self.driver, 5).until(presence_of_element_located((By.XPATH, element)))

    def header_element(self,header_element):
        return self.driver.find_element(By.XPATH,header_element)

    def populate_contactUs_fields(self,name,email,subject,message):

        values = [(ContactUs_Locators.field_name,name),
                  (ContactUs_Locators.field_email,email),
                  (ContactUs_Locators.field_subject,subject),
                  (ContactUs_Locators.field_message,message)]

        for field,values in values:
            self.driver.find_element(By.CSS_SELECTOR,field).send_keys(values)

    def select_file(self,file_path):
        self.driver.find_element(By.CSS_SELECTOR,ContactUs_Locators.field_file).send_keys(file_path)

    def submit(self):
        return self.driver.find_element(By.CSS_SELECTOR,ContactUs_Locators.button_submit).click()

    def alert_handler(self,action):

        WebDriverWait(self.driver,5).until(alert_is_present())
        alert_handler = Alert(self.driver)

        if action == 'Ok':
            alert_handler.accept()
        elif action == 'Cancel':
            alert_handler.dismiss()

    def alert_success_message(self):
        return self.driver.find_element(By.CSS_SELECTOR,ContactUs_Locators.alert_success)

    def alert_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,ContactUs_Locators.alert_home_button).click()
