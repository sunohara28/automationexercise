import pytest
from selenium.common import NoSuchElementException
from Objects.General_Locator import General_Locators
from Objects.Menu import Menu_Elements
from Objects.Products import Products_locators, Products_Elements
from Objects.Shopping_cart import ShoppingCart_Locators
from Test.WebDriver import InitDriver
import Test.csv_Reader as csvReader


class TestMain(InitDriver):
    def test_homepage(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_products)
        General_Loc.element_locator_css(Menu_Elements.link_products).click()

    def test_products(self):
        Products_loc = Products_locators(self.driver)
        General_Loc = General_Locators(self.driver)
        product_index_csv = csvReader.csvReader(csvReader.searchProductData_viaIndex)


        try:
            assert General_Loc.element_locator_css(Products_Elements.product_header_element).is_displayed()
        except NoSuchElementException as triggeredException:
            print("All Products header is not displayed",triggeredException)


        items_position = []
        for Product in product_index_csv:
            items_position.append(Product)

        index = 0
        for item in items_position:
            index = index + 1
            Products_loc.product_hover(item['product_index'])

            Products_loc.hover_add_to_cart(item['product_index'])

            if index != len(items_position):
                General_Loc.wait_element_css(Products_Elements.modal_continue_button_element)
                General_Loc.element_locator_css(Products_Elements.modal_continue_button_element).click()
            else:
                General_Loc.wait_element_css(Products_Elements.modal_view_cart_element)
                General_Loc.element_locator_css(Products_Elements.modal_view_cart_element).click()

    def test_product_details(self):
        General_Loc = General_Locators(self.driver)
        ShoppingCart_Loc = ShoppingCart_Locators(self.driver)
        product_index_csv = csvReader.csvReader(csvReader.searchProductData_viaIndex)

        items_position = []
        for Product in product_index_csv:
            items_position.append(Product)

        for item in items_position:
            print(ShoppingCart_Loc.retrieve_item_id(item['product_index']))
            print(ShoppingCart_Loc.item_description(item['product_index']).text)
            print(ShoppingCart_Loc.item_price(item['product_index']).text)
            print(ShoppingCart_Loc.item_quantity(item['product_index']).text)
            print(ShoppingCart_Loc.item_total(item['product_index']).text)
