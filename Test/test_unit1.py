from Test.WebDriver import InitDriver
from Objects.Menu import Menu_Elements
from Objects.General_Locator import General_Locators

class TestMain(InitDriver):

    def test_navigate_to_signup(self):
        General_Loc = General_Locators(self.driver)

        General_Loc.wait_element_css(Menu_Elements.link_signup_login)
        General_Loc.element_locator_css(Menu_Elements.link_signup_login).click()
