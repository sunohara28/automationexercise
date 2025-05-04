
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert

class ContactUs_Elements:

    field_name = "input[name='name']"
    field_email = "input[name='email']"
    field_subject = "input[name='subject']"
    field_message = "textarea[name='message']"
    field_file = "input[name='upload_file']"

    alert_success = ".status.alert.alert-success"
    alert_home_button = ".btn.btn-success"

    button_submit = "input[name='submit']"

    header_get_in_touch = "//h2[text()='Get In Touch']"

class ContactUs_Locators:

    def __init__(self,driver):
        self.driver = driver

    def populate_contactUs_fields(self,name,email,subject,message,file):

        values = [(ContactUs_Elements.field_name,name),
                  (ContactUs_Elements.field_email,email),
                  (ContactUs_Elements.field_subject,subject),
                  (ContactUs_Elements.field_message,message),
                  (ContactUs_Elements.field_file,file)]

        for field, values in values:
            self.driver.find_element(By.CSS_SELECTOR, field).send_keys(values)

        self.driver.find_element(By.CSS_SELECTOR,ContactUs_Elements.button_submit).click()

    def alert_handler(self,action):

        WebDriverWait(self.driver,5).until(alert_is_present())
        alert_handler = Alert(self.driver)

        if action == 'Ok':
            alert_handler.accept()
        elif action == 'Cancel':
            alert_handler.dismiss()
