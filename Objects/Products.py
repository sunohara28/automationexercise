from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Products_locators:

    header_all_products = "//h2[text()='All Products']"
    view_product = "fa fa-plus-square"

    def __init__(self,driver):
        self.driver = driver


    def explicity_wait_element_xpath(self,element):
        return WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,element)))

    def element_locator_xpath(self,element):
        return self.driver.find_element(By.XPATH,element)

    def product_list(self):
        Product_List = self.driver.find_elements(By.CLASS_NAME,Products_locators.view_product)

        for product in Product_List:
            Product_List.

