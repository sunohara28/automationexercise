from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Signup_acc_Locators:

    header_account_info = "//b[text()='Enter Account Information']"
    header_address_info = "//b[text()='Address Information']"

    field_gender_mr = "id_gender1"
    field_gender_mrs = "id_gender2"

    field_password = "password"
    field_day = "days"
    field_month = "months"
    field_year = "years"

    field_newsletter = "newsletter"
    field_optin = "optin"

    field_fname = "first_name"
    field_lname = "last_name"
    field_company = "company" 
    field_addr1 = "address1"
    field_addr2 = "address2"
    field_country = "country"
    field_state = "state"
    field_city = "city"
    field_zipcode = "zipcode"
    field_mobile_numer = "mobile_number"

    button_create_account = "button[data-qa='create-account']"


    def __init__(self,driver):
        self.driver = driver

    
    def header_signup_locator(self,header):
        return self.driver.find_element(By.XPATH,header)

    def fill_signup_account_info(self,title,password,days,months,years,optin,newsletter):
        
        gender_dict = {"Mr":"id_gender1",
                       "Mrs":"id_gender2"}

        self.driver.find_element(By.ID,gender_dict.get(title)).click()
        
        self.driver.find_element(By.ID,Signup_acc_Locators.field_password).send_keys(password)

        select_days = Select(self.driver.find_element(By.ID,Signup_acc_Locators.field_day))
        select_months = Select(self.driver.find_element(By.ID,Signup_acc_Locators.field_month))
        select_years = Select(self.driver.find_element(By.ID,Signup_acc_Locators.field_year))

        select_days.select_by_visible_text(days)
        select_months.select_by_visible_text(months)
        select_years.select_by_visible_text(years)

        if newsletter is True: self.driver.find_element(By.ID,Signup_acc_Locators.field_newsletter).click()
        if optin is True: self.driver.find_element(By.ID,Signup_acc_Locators.field_optin).click()


    def fill_signup_account_addr_info(self,fname,lname,addr1,addr2,company,state,city,zipcode,mobile_number):

        addr_info_fields = [(Signup_acc_Locators.field_fname,fname),
                            (Signup_acc_Locators.field_lname,lname),
                            (Signup_acc_Locators.field_company,company),
                            (Signup_acc_Locators.field_addr1,addr1),
                            (Signup_acc_Locators.field_addr2,addr2),
                            (Signup_acc_Locators.field_state,state),
                            (Signup_acc_Locators.field_city,city),
                            (Signup_acc_Locators.field_zipcode,zipcode),
                            (Signup_acc_Locators.field_mobile_numer,mobile_number)]

        for field,value in addr_info_fields:
            self.driver.find_element(By.ID,field).send_keys(value)

    def select_cntry(self,cntry):

        select_cntry = Select(self.driver.find_element(By.ID,Signup_acc_Locators.field_country))
        select_cntry.select_by_visible_text(cntry)

    def submit_create_account(self):
        return self.driver.find_element(By.CSS_SELECTOR,Signup_acc_Locators.button_create_account).click()