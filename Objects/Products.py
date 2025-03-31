import time
from argparse import Action

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class Products_locators:


    product_header_element = ".title.text-center"
    product_name_element = "//div[@class='col-sm-4']/div/div/div/p"
    product_add_element = "//div[@class='col-sm-4']/div/div/div/a"

    search_textbox_element = "search_product"
    search_button_element = "submit_search"


    modal_container_element = ".modal-content"
    modal_view_cart_element = "p[class='text-center'] a"
    modal_continue_button_element = ".btn.btn-success.close-modal.btn-block"

    product_details_avail = "//div[@class='product-information']/p[2]"
    product_details_add_button = "//button[@class='btn btn-default cart']"

    def __init__(self,driver):
        self.driver = driver


    def explicitly_wait_element_xpath(self,element):
        return WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,element)))

    def explicitly_wait_element_css(self,element):
        return WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,element)))

    def element_locator_xpath(self,element):
        return self.driver.find_element(By.XPATH,element)

    def element_locator_css(self,element):
        return self.driver.find_element(By.CSS_SELECTOR, element)

    def product_name_specific(self,*args):
        list_prod = {*args}
        for index in list_prod:
            # index = index + 1
            print(self.driver.find_element(By.XPATH, f"//div[@class='col-sm-4'][{index}]/div/div/div/p").text)

    def view_product_index(self,index):
        product_xpath = f"(//a[contains(text(),'View Product')])[{index}]"
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,product_xpath)))

        scroll_origin = ScrollOrigin.from_element(
            self.driver.find_element(By.XPATH, product_xpath))
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 200).perform()

        self.driver.find_element(By.XPATH, product_xpath).click()

    def product_details_availability(self):
        return self.driver.find_element(By.XPATH,Products_locators.product_details_avail).text

    def product_details_add_to_cart(self):
        self.driver.find_element(By.XPATH,Products_locators.product_details_add_button).click()

    def search_product(self,product):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,Products_locators.search_textbox_element)))
        self.driver.find_element(By.ID,Products_locators.search_textbox_element).send_keys(product)
        self.driver.find_element(By.ID,Products_locators.search_button_element).click()

    def product_list(self,element): #return a variable containing the product names as list
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, element)))
        products = self.driver.find_elements(By.XPATH,element)
        return products

    def product_hover(self,index):
        action = ActionChains(self.driver)

        action.scroll_to_element(self.driver.find_element(By.XPATH,f"//div[@class='col-sm-4'][{index}]")).perform()
        action.move_to_element(self.driver.find_element(By.XPATH,f"//div[@class='col-sm-4'][{index}]")).perform()

    def product_add_to_cart(self,index):
        product = f"//div[@class='col-sm-4'][{index}]/div/div/div/div/a"
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, product)))
        self.driver.find_element(By.XPATH,product).click()

    def modal_button_click(self,element):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
        self.driver.find_element(By.CSS_SELECTOR,element).click()




