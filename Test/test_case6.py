import time

import pytest
from selenium.common import NoSuchElementException
import Test.csv_Reader as csvReader
from Test.WebDriver import InitDriver
from Objects.Menu import Menu_Locators
from Objects.ContactUs import ContactUs_Locators

class TestMain(InitDriver):

    def test_homepage(self):
        Menu_Loc = Menu_Locators(self.driver)

        Menu_Loc.wait_element(Menu_Loc.link_contact_us)

        try:
            assert Menu_Loc.link_locator(Menu_Loc.link_contact_us).is_displayed()
        except NoSuchElementException as triggeredException:
            print("Header signup is not displayed", triggeredException)

        Menu_Loc.link_locator(Menu_Loc.link_contact_us).click()

    def test_contact_us(self):
        ContactUs_Loc = ContactUs_Locators(self.driver)
        data = csvReader.csvReader(csvReader.contactUsData)

        ContactUs_Loc.populate_contactUs_fields(data[0]['name'],data[0]['email'],data[0]['subject'],data[0]['message'])
        ContactUs_Loc.select_file(data[0]['file_path'])
        ContactUs_Loc.submit()

    def test_alert(self):

        data = csvReader.csvReader(csvReader.contactUsData)
        ContactUs_Loc = ContactUs_Locators(self.driver)
        ContactUs_Loc.alert_handler(data[0]['alert_action'])

    def test_success_message(self):
        ContactUs_Loc = ContactUs_Locators(self.driver)

        ContactUs_Loc.wait_field_element_CSS(ContactUs_Loc.alert_success)

        try:
            assert ContactUs_Loc.alert_success_message().is_displayed()
        except NoSuchElementException as triggeredException:
            print("Alert success message is not displayed",triggeredException)

    def test_return_to_home(self):
        ContactUs_Loc = ContactUs_Locators(self.driver)
        ContactUs_Loc.alert_button()



