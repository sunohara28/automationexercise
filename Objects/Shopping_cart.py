import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class ShoppingCart_Elements:
    ...

class ShoppingCart_Locators:
    def __init__(self,driver):
        self.driver = driver


    def retrieve_item_id(self,index):
        items = self.driver.find_elements(By.TAG_NAME, "tr")
        for item in items:
            if item.get_attribute("id") == f"product-{index}":
                return item.get_attribute("id")

    def item_image(self,index):
        img = self.driver.find_element(By.CSS_SELECTOR, f"tr[id='product-{index}'] img[alt='Product Image']")
        return img.get

    def item_description(self,index):
        return self.driver.find_element(By.CSS_SELECTOR, f"tr[id='product-{index}'] td[class='cart_description'] h4")

    def item_price(self,index):
        return self.driver.find_element(By.CSS_SELECTOR, f"tr[id='product-{index}'] td[class='cart_price'] p")

    def item_quantity(self,index):
        return self.driver.find_element(By.CSS_SELECTOR, f"tr[id='product-{index}'] td[class='cart_quantity']")

    def item_total(self,index):
        return self.driver.find_element(By.CSS_SELECTOR, f"tr[id='product-{index}'] p[class='cart_total_price']")
