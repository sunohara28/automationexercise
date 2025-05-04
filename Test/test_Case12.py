import time

import pytest
from selenium.common import NoSuchElementException

from Objects.General_Locator import General_Locators
from Objects.Menu import Menu_Elements
from Objects.Product_details import ProductDetails_Locators, ProductDetails_Elements
from Objects.Products import Products_locators, Products_Elements
from Test.WebDriver import InitDriver


class TestMain(InitDriver):
    def test_homepage(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_products)
        General_Loc.element_locator_css(Menu_Elements.link_products).click()

    def test_products(self):
        Products_loc = Products_locators(self.driver)
        General_Loc = General_Locators(self.driver)


        try:
            assert General_Loc.element_locator_css(Products_Elements.product_header_element).is_displayed()
        except NoSuchElementException as triggeredException:
            print("All Products header is not displayed",triggeredException)


        items_position = {8,2}
        index = 0
        for item in items_position:
            index = index + 1
            Products_loc.product_hover(item)

            Products_loc.hover_add_to_cart(item)

            if index != len(items_position):
                General_Loc.wait_element_css(Products_Elements.modal_continue_button_element)
                General_Loc.element_locator_css(Products_Elements.modal_continue_button_element).click()
            else:
                General_Loc.wait_element_css(Products_Elements.modal_view_cart_element)
                General_Loc.element_locator_css(Products_Elements.modal_view_cart_element).click()

        time.sleep(2)

    @pytest.mark.skip
    def test_product_details(self):
        General_Loc = General_Locators(self.driver)