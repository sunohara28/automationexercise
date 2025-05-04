from selenium.common import NoSuchElementException
import Test.csv_Reader as csvReader
from Objects.General_Locator import General_Locators
from Test.WebDriver import InitDriver
from Objects.Menu import Menu_Elements
from Objects.Contact_us import ContactUs_Locators, ContactUs_Elements


class TestMain(InitDriver):

    def test_homepage(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_contact_us)
        General_Loc.element_locator_css(Menu_Elements.link_contact_us).click()


    def test_contact_us(self):
        data = csvReader.csvReader(csvReader.contactUsData)
        ContactUs_Loc = ContactUs_Locators(self.driver)
        General_Loc = General_Locators(self.driver)

        General_Loc.multiple_wait_element_css(ContactUs_Elements.field_name,
                  ContactUs_Elements.field_email,
                  ContactUs_Elements.field_subject,
                  ContactUs_Elements.field_message,
                  ContactUs_Elements.field_file)

        ContactUs_Loc.populate_contactUs_fields(data[0]['name'], data[0]['email'], data[0]['subject'],
                                                data[0]['message'],data[0]['file_path'])

    def test_alert(self):
        data = csvReader.csvReader(csvReader.contactUsData)
        ContactUs_Loc = ContactUs_Locators(self.driver)

        ContactUs_Loc.alert_handler(data[0]['alert_action'])


    def test_success_message(self):
        General_Loc = General_Locators(self.driver)

        try:
            assert General_Loc.element_locator_css(ContactUs_Elements.alert_success).is_displayed()
        except NoSuchElementException as triggeredException:
            print("Alert success message is not displayed",triggeredException)


    def test_return_to_home(self):
        General_Loc = General_Locators(self.driver)
        General_Loc.element_locator_css(ContactUs_Elements.alert_home_button).click()



