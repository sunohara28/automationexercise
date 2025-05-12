import time

import Test.csv_Reader as csvReader

from Objects.General_Locator import General_Locators
from Objects.Menu import Menu_Locators, Menu_Elements
from Objects.Product_details import ProductDetails_Locators
from Objects.Products import Products_locators, Products_Elements
from Test.WebDriver import InitDriver


class TestMain(InitDriver):
    def test_product_page(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_products)
        General_Loc.element_locator_css(Menu_Elements.link_products).click()

    def test_add_to_cart(self):
        General_Loc = General_Locators(self.driver)
        Menu_Loc = Menu_Locators(self.driver)
        Products_loc = Products_locators(self.driver)
        ProductDetails_Loc = ProductDetails_Locators(self.driver)
        products_csv = csvReader.csvReader(csvReader.searchProductData_viaName)


        available = "In Stock"
        Product_List = []

        for Product in products_csv: #retrieve the Product names in CSV file and append to a variable list
            Product_List.append(Product)

        for value in products_csv: #iterate the product names from the CSV to search
            prod_name = value['Product_Name']
            Products_loc.search_product(prod_name) #search the product

            products_name = Products_loc.product_list(Products_Elements.product_name_element)
            # return the list of Product that has the searched product name

            for index, product in enumerate(products_name, start = 1):

                print(product.text , prod_name, index)
                if product.text == prod_name:
                    print("Yes", product.text)

                    Products_loc.view_product_index(index)
                    if available in ProductDetails_Loc.element_xpath_locator(ProductDetails_Loc.availability_element).text:
                        Products_loc.element_locator_xpath(Products_loc.product_details_add_button).click()
                        Products_loc.modal_button_click(Products_loc.modal_continue_button_element)

                    Menu_Loc.element_locator_css(Menu_Loc.link_products).click()
                    break
            Menu_Loc.element_locator_css(Menu_Loc.link_products).click()

        Menu_Loc.element_locator_css(Menu_Loc.link_cart).click()










