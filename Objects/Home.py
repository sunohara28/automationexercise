from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Home_Locators:

    def __init__(self,driver):
        self.driver = driver

    def body_locator(self):
        return self.driver.find_element(By.XPATH,"//body")

    def goto_link(self,link):
        return self.driver.find_element(By.LINK_TEXT,link).click()