import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import Test.csv_Reader as csvReader
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
    data = csvReader.csvReader(csvReader.contactUsData)

    value = data[0]['alert_action']

    if value == "Ok":
        print("Ok")
    elif value == "Cancel":
        print("Cancel")

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

def test_link_click():
    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/products")
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.find_element(By.CSS_SELECTOR,"a[href='/']").click()
    time.sleep(2)