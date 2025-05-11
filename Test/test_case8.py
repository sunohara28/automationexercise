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

        Products_loc.view_product_index(1)


    def test_product_details(self):
        General_Loc = General_Locators(self.driver)

        elements = {ProductDetails_Elements.product_name_element,
                    ProductDetails_Elements.category_element,
                    ProductDetails_Elements.price_element,
                    ProductDetails_Elements.availability_element,
                    ProductDetails_Elements.condition_element,
                    ProductDetails_Elements.brand_element}

        for element in elements:
            try:
                assert General_Loc.element_locator_xpath(element).is_displayed()
            except NoSuchElementException as triggeredException:
                print("info not displayed",triggeredException)