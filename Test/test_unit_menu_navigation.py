from Test.WebDriver import InitDriver
from Objects.Menu import Menu_Elements
from Objects.General_Locator import General_Locators

class TestMain(InitDriver):

    def test_products(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_products)
        General_Loc.element_locator_css(Menu_Elements.link_products).click()

    def test_cart(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_cart)
        General_Loc.element_locator_css(Menu_Elements.link_cart).click()

    def test_navigate_to_signup_login(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_signup_login)
        General_Loc.element_locator_css(Menu_Elements.link_signup_login).click()

    def test_navigate_to_test_cases(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_test_case)
        General_Loc.element_locator_css(Menu_Elements.link_test_case).click()

    def test_navigate_to_api_testing(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_api_testing)
        General_Loc.element_locator_css(Menu_Elements.link_api_testing).click()

    def test_navigate_to_contact_us(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_contact_us)
        General_Loc.element_locator_css(Menu_Elements.link_contact_us).click()

