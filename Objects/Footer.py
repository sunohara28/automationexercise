from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

class Footer_Locators:

    footer_element = "footer"
    footer_sub_text = "div[class='single-widget'] h2"
    footer_email_textbox = "susbscribe_email"
    footer_button = "subscribe"

    alert_success_subscribed = ".alert-success.alert"


    def __init__(self,driver):
        self.driver = driver

    def explicit_wait_css(self,element):
        return WebDriverWait(self.driver, 5).until(presence_of_element_located(element))

    def body_locator(self):
        return self.driver.find_element(By.XPATH,"//body")

    def element_locator_css(self,element):
        return self.driver.find_element(By.CSS_SELECTOR,element)

    def element_locator_id(self,element):
        return self.driver.find_element(By.ID,element)

    def element_send_keys(self,element,value):
        return element.send_keys(value)

    def element_click(self,element):
        return element.click()

    def goto_link(self,link):
        return self.driver.find_element(By.LINK_TEXT,link).click()

    def goto_element_scroll(self,element):
        (ActionChains(self.driver)
         .scroll_to_element(self.driver.find_element(By.ID,element))
         .perform())

    def alert_handler(self):
        ...