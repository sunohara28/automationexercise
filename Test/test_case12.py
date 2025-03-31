import time

import Test.csv_Reader as csvReader
from selenium.common import NoSuchElementException
from Objects.Menu import Menu_Locators
from Objects.ProductDetails import ProductDetails_Locators
from Objects.Products import Products_locators
from Test.WebDriver import InitDriver


class TestMain(InitDriver):
    def test_product_page(self):
        Menu_Loc = Menu_Locators(self.driver)

        try:
            assert Menu_Loc.link_locator(Menu_Loc.link_products).is_displayed()
        except NoSuchElementException as triggeredException:
            print("Link not displayed",triggeredException)

        Menu_Loc.link_locator(Menu_Loc.link_products).click()
        self.driver.implicitly_wait(5)

    def test_add_to_cart(self):
        Menu_Loc = Menu_Locators(self.driver)
        Products_loc = Products_locators(self.driver)
        ProductDetails_Loc = ProductDetails_Locators(self.driver)
        products_csv = csvReader.csvReader(csvReader.searchProductData)


        available = "In Stock"
        Product_List = []

        for Product in products_csv: #retrieve the Product names in CSV file and append to a variable list
            Product_List.append(Product)

        for value in products_csv: #iterate the product names from the CSV to search
            prod_name = value['Product_Name']
            Products_loc.search_product(prod_name) #search the product

            products_name = Products_loc.product_list(Products_loc.product_name_element)
            # return the list of Product that has the searched product name

            for index, product in enumerate(products_name, start = 1):

                print(product.text , prod_name, index)
                if product.text == prod_name:
                    print("Yes", product.text)

                    Products_loc.view_product_index(index)
                    if available in ProductDetails_Loc.element_xpath_locator(ProductDetails_Loc.availability_element).text:
                        Products_loc.element_locator_xpath(Products_loc.product_details_add_button).click()
                        Products_loc.modal_button_click(Products_loc.modal_continue_button_element)

                    Menu_Loc.link_locator(Menu_Loc.link_products).click()
                    break
            Menu_Loc.link_locator(Menu_Loc.link_products).click()

        Menu_Loc.link_locator(Menu_Loc.link_cart).click()










