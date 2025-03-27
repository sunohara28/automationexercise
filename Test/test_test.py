from selenium import webdriver
from selenium.webdriver.common.by import By
import Test.csv_Reader as csvReader
from Objects.Signup_Login import Signup_Login_Locators


def login_account(email,password):
    account_info_fields = [(Signup_Login_Locators.field_login_email,email),
                           (Signup_Login_Locators.field_login_pass,password)]
    print(account_info_fields)

    for field,value in account_info_fields:
        print(field,value)

def test_args():
    login_account("aki@gmail.com","Password1")

def test_csv_alert_value():
    data = csvReader.csvReader(csvReader.contactUsData)

    value = data[0]['alert_action']

    if value == "Ok":
        print("Ok")
    elif value == "Cancel":
        print("Cancel")

def test_product_list():
    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com/products")

    product_list = driver.find_elements(By.CLASS_NAME,"fa fa-plus-square")

    for product in product_list:
        print(driver.find_element(By.CLASS_NAME,"fa fa-plus-square""))




