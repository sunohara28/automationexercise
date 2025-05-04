from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

class Footer_Elements:

    footer_element = "footer"
    footer_sub_text = "div[class='single-widget'] h2"
    footer_email_textbox = "susbscribe_email"
    footer_button = "subscribe"

    alert_success_subscribed = ".alert-success.alert"


class Footer_Locators:

    def __init__(self,driver):
        self.driver = driver

    def subscribe(self,value):
        self.driver.find_element(By.ID,Footer_Elements.footer_email_textbox).send_keys(value)
        self.driver.find_element(By.ID,Footer_Elements.footer_button).click()

    def goto_element_scroll(self,element):
        (ActionChains(self.driver)
         .scroll_to_element(self.driver.find_element(By.ID,element))
         .perform())