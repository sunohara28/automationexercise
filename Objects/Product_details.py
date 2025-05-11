from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class ProductDetails_Elements:

    image_element = "//div[@class='product-information']/img[@class='newarrival']"
    product_name_element = "//div[@class='product-information']/h2"
    category_element = "//div[@class='product-information']/p[1]"
    price_element = "//div[@class='product-information']/span/span"
    availability_element = "//div[@class='product-information']/p[2]"
    condition_element = "//div[@class='product-information']/p[3]"
    brand_element = "//div[@class='product-information']/p[4]"
    button_add_to_cart_element = "//div[@class='product-information']/span/button"

class ProductDetails_Locators:

    def __init__(self,driver):
        self.driver = driver

