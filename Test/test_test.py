import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import Test.csv_Reader as csvReader
from Objects.Products import Products_locators
from Objects.Signup_Login import Signup_Login_Locators


def login_account(email, password):
    account_info_fields = [(Signup_Login_Locators.field_login_email, email),
                           (Signup_Login_Locators.field_login_pass, password)]
    print(account_info_fields)

    for field, value in account_info_fields:
        print(field, value)


def test_args():
    login_account("aki@gmail.com", "Password1")


def test_csv_alert_value():
    Products = csvReader.csvReader(csvReader.searchProductData)

    value = []

    for Product in Products:
        value.append(Product)

    print(value)
    print(len(value))

    for value in value:
        print(value['Product_Name'])


def test_index():

    list_prod = {2, 4, 6}

    for index in list_prod:
        print(index)

def args_list(*args):
    list_index = {*args}
    return list_index

def test_product_list():
    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/products")
    driver.maximize_window()
    driver.implicitly_wait(5)

    product_list_view = driver.find_elements(By.XPATH, "(//a[contains(text(),'View Product')])")

    list_prod = {2, 4, 6}

    for index in args_list(1):
       # index = index + 1
        print(driver.find_element(By.XPATH,f"//div[@class='col-sm-4'][{index}]/div/div/div/p").click)

def test_details():
    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/product_details/1")
    driver.maximize_window()
    driver.implicitly_wait(5)

    availability = driver.find_element(By.XPATH,"//div[@class='product-information']/p[2]").text
    available = "In Stock"

    if available in availability:
        print("Yes")
    elif available not in availability:
        print("No")

def test_view_product_details():
    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/products")
    driver.maximize_window()
    driver.implicitly_wait(5)
    Products_loc = Products_locators(driver)


    lists = ["Blue","Men Tshirt"]

    for product_name in lists:
        index = 0
        Products_loc.search_product(product_name)
        products_name = Products_loc.product_list(Products_loc.product_name_element)
        time.sleep(1)

        for product in products_name:
            index = index + 1
            print(product.text, product_name, index)

            if product.text == product_name:
                print("Yes")
                WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, f"(//a[contains(text(),'View Product')])[{index}]")))

                scroll_origin = ScrollOrigin.from_element(driver.find_element(By.XPATH, f"(//a[contains(text(),'View Product')])[{index}]"))
                ActionChains(driver).scroll_from_origin(scroll_origin, 0, 200).perform()

                driver.find_element(By.XPATH,f"(//a[contains(text(),'View Product')])[{index}]").click()
                driver.find_element(By.CSS_SELECTOR,"a[href='/products']").click()
        driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()

def test_scroll():
    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/products?search=Men%20Tshirt")
    driver.maximize_window()
    driver.implicitly_wait(5)
    index = 1
    scroll_origin = ScrollOrigin.from_element(
        driver.find_element(By.XPATH, f"(//a[contains(text(),'View Product')])[{index}]"))
    ActionChains(driver).scroll_from_origin(scroll_origin, 0, 200).perform()
    time.sleep(5)
    driver.find_element(By.XPATH, f"(//a[contains(text(),'View Product')])[{index}]").click()



def test_link_click():
    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/products")
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.find_element(By.CSS_SELECTOR,"a[href='/']").click()
    time.sleep(2)

def test_case_insensitive():

    product = {"Blue","Blue Top", "BLUE Top","Top BLuE"}
    product_search = "Blue"

    for product_search in product:
        if product_search in product:
            print("equal")
        else:
            print("faluse")

def test_footer():

    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/products")
    driver.maximize_window()
    driver.implicitly_wait(5)

    (ActionChains(driver)
     .scroll_to_element(driver.find_element(By.CSS_SELECTOR,"div[class='single-widget'] h2" ))
     .perform())

    driver.find_element(By.ID,"susbscribe_email").send_keys("aki@gmail.com")
    driver.find_element(By.ID, "subscribe").click()

    assert driver.find_element(By.CSS_SELECTOR, ".alert-success.alert").is_displayed()

def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/products")
    driver.maximize_window()
    driver.implicitly_wait(5)

    action = ActionChains(driver)
    action.scroll_to_element(driver.find_element(By.XPATH, f"//div[@class='col-sm-4'][2]")).perform()
    action.move_to_element(driver.find_element(By.XPATH, f"//div[@class='col-sm-4'][2]")).perform()

    driver.find_element(By.XPATH,"//div[@class='col-sm-4'][2]/div/div/div/div/a").click()

    WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".btn.btn-success.close-modal.btn-block")))
    self.driver.find_element(By.CSS_SELECTOR, element)

    time.sleep(5)

def test_modal():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/entry_ad")
    driver.maximize_window()
    driver.implicitly_wait(5)

    WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='modal']")))

    driver.find_element(By.XPATH,"//p[normalize-space()='Close']").click()