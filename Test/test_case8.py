from selenium.common import NoSuchElementException

from Objects.Menu import Menu_Locators
from Objects.ProductDetails import ProductDetails_Locators
from Objects.Products import Products_locators
from Test.WebDriver import InitDriver


class TestMain(InitDriver):
    def test_homepage(self):
        Menu_Loc = Menu_Locators(self.driver)

        try:
            assert Menu_Loc.link_locator(Menu_Loc.link_products).is_displayed()
        except NoSuchElementException as triggeredException:
            print("Link not displayed",triggeredException)

        Menu_Loc.link_locator(Menu_Loc.link_products).click()

    def test_products(self):
        Products_loc = Products_locators(self.driver)

        Products_loc.explicity_wait_element_xpath(Products_loc.header_all_products_element)

        try:
            assert Products_loc.element_locator_xpath(Products_loc.header_all_products_element).is_displayed()
        except NoSuchElementException as triggeredException:
            print("All Products header is not displayed",triggeredException)

        Products_loc.explicity_wait_element_xpath(Products_loc.product_view_specific)
        Products_loc.product_view_specific(1)

    def test_product_details(self):
        ProductDetails_Loc = ProductDetails_Locators(self.driver)


        elements = {ProductDetails_Loc.product_name_element,
                    ProductDetails_Loc.category_element,
                    ProductDetails_Loc.price_element,
                    ProductDetails_Loc.availability_element,
                    ProductDetails_Loc.condition_element,
                    ProductDetails_Loc.brand_element}

        for element in elements:
            try:
                assert ProductDetails_Loc.element_xpath_locator(element).is_displayed()
            except NoSuchElementException as triggeredException:
                print("info not displayed",triggeredException)