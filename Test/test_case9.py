from selenium.common import NoSuchElementException
import Test.csv_Reader as csvReader
from Objects.General_Locator import General_Locators
from Objects.Menu import Menu_Locators, Menu_Elements
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

    def test_search_product(self):
        searchProductData = csvReader.csvReader(csvReader.searchProductData_viaName)
        Products_loc = Products_locators(self.driver)

        Products_loc.search_product(searchProductData[0]['Product_Name'])

    def test_searched_products(self):
        searchProductData = csvReader.csvReader(csvReader.searchProductData_viaName)
        search_product = searchProductData[0]['Product_Name']
        Products_loc = Products_locators(self.driver)

        Products_name = Products_loc.product_list(Products_Elements.product_name_element)


        for product in Products_name:
            try:
                assert search_product.casefold() in product.text.casefold()
            except:
                print(product.text,"is not equal with searched product")



