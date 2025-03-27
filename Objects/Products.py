from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Products_locators:

    header_all_products = "//h2[text()='All Products']"

    def __init__(self,driver):
        self.driver = driver


    def explicity_wait_element_xpath(self,element):
        return WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,element)))

    def element_locator_xpath(self,element):
        return self.driver.find_element(By.XPATH,element)

    def product_list(self):
        Product_List = self.driver.find_elements(By.XPATH,Products_locators.products)

        return len(Product_List)

    def product_info(self,*args):
        list_prod = {*args}
        for index in list_prod:
            # index = index + 1
            print(self.driver.find_element(By.XPATH, f"//div[@class='col-sm-4'][{index}]/div/div/div/p").text)

    def product_view(self,index):
        self.driver.find_element(By.XPATH,f"(//a[contains(text(),'View Product')])[{index}]").click()