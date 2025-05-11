from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class General_Locators:

    def __init__(self, driver):
        self.driver = driver

    def multiple_wait_element_css(self,*element):

        list_element = element

        for element in list_element:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))

    def multiple_wait_element_xpath(self,*element):

        list_element = element

        for element in list_element:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, element)))

    def wait_element_css(self, element):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))

    def wait_element_id(self, element):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, element)))

    def wait_element_xpath(self, element):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, element)))

    def element_locator_css(self, element):
        return self.driver.find_element(By.CSS_SELECTOR, element)

    def element_locator_id(self, element):
        return self.driver.find_element(By.ID, element)

    def element_locator_xpath(self, element):
        return self.driver.find_element(By.XPATH, element)