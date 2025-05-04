from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Signup_acc_Elements:

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

class Signup_acc_Locators:

    def __init__(self,driver):
        self.driver = driver

    def fill_signup_account_info(self,title,password,days,months,years,optin,newsletter):

        gender_dict = {"Mr":"id_gender1",
                       "Mrs":"id_gender2"}

        list_element = (gender_dict.get(title),
                        Signup_acc_Elements.field_password,
                        Signup_acc_Elements.field_day,
                        Signup_acc_Elements.field_month,
                        Signup_acc_Elements.field_year,
                        Signup_acc_Elements.field_newsletter,
                        Signup_acc_Elements.field_optin)

        for element in list_element:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, element)))

        self.driver.find_element(By.ID,gender_dict.get(title)).click()
        self.driver.find_element(By.ID,Signup_acc_Elements.field_password).send_keys(password)

        select_days = Select(self.driver.find_element(By.ID,Signup_acc_Elements.field_day))
        select_months = Select(self.driver.find_element(By.ID,Signup_acc_Elements.field_month))
        select_years = Select(self.driver.find_element(By.ID,Signup_acc_Elements.field_year))

        select_days.select_by_visible_text(days)
        select_months.select_by_visible_text(months)
        select_years.select_by_visible_text(years)

        if newsletter is True: self.driver.find_element(By.ID,Signup_acc_Elements.field_newsletter).click()
        if optin is True: self.driver.find_element(By.ID,Signup_acc_Elements.field_optin).click()


    def fill_signup_account_addr_info(self,fname,lname,addr1,addr2,company,state,city,zipcode,mobile_number):

        addr_info_fields = [(Signup_acc_Elements.field_fname,fname),
                            (Signup_acc_Elements.field_lname,lname),
                            (Signup_acc_Elements.field_company,company),
                            (Signup_acc_Elements.field_addr1,addr1),
                            (Signup_acc_Elements.field_addr2,addr2),
                            (Signup_acc_Elements.field_state,state),
                            (Signup_acc_Elements.field_city,city),
                            (Signup_acc_Elements.field_zipcode,zipcode),
                            (Signup_acc_Elements.field_mobile_numer,mobile_number)]

        for field,value in addr_info_fields:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, field)))
            self.driver.find_element(By.ID,field).send_keys(value)

    def select_cntry(self,cntry):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, Signup_acc_Elements.field_country)))
        select_cntry = Select(self.driver.find_element(By.ID,Signup_acc_Elements.field_country))
        select_cntry.select_by_visible_text(cntry)
