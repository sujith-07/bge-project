import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class Entity_Management:
    menuItem_entityManagement_Xpath="//span[normalize-space()='Entity Management']"
    #Hospital and Safety
    submenu_HS_Xpath="//span[normalize-space()='Health and Safety']"
    add_HS_Xpath="(//button[@class='btn btn-primary btn-icon'])[1]"
    input_HS_hospital_Xpath="//input[@name='name']"
    dd_HS_mobileNumber_Xpath = "//div[contains(@class,'form-control-wrap d-flex')]//div[contains(@class,'p-0 col-4 col-md-2 col-lg-3')]"
    dd_HS_select_mobile_countryCode_Xpath = "//div[contains(@class,'form-control-wrap d-flex')]//div[contains(@class,'css-1g6gooi')]"
    input_HS_phoneNumber_Xpath = "(//input[@name='phoneNumber'])[1]"
    input_HS_address_Xpath="//input[@name='address']"
    btn_HS_add_Xpath="//button[normalize-space()='Add']"

    #DNO
    submenu_DNO_Xpath= '//a[@href="/entity_management/dnos"]'
    add_DNO_Xpath = "(//button[@class='btn btn-primary btn-icon'])[1]"
    input_DNO_Xpath="//input[@name='name']"
    btn_DNO_add_Xpath = "//button[normalize-space()='Add']"



    #SLA
    submenu_SLA_Xpath= "//span[normalize-space()='SLA']"
    add_SLA_Xpath = "(//button[@class='btn btn-primary btn-icon'])[1]"
    input_SLA_Level_Xpath="//input[@name='name']"
    input_SLA_Description_Xpath="//textarea[@name='description']"
    btn_add_SLA_Xpath="//button[normalize-space()='Add']"




    def __init__(self,driver):
        self.driver=driver
    def Menu_EntityManagement(self):
        self.driver.find_element(By.XPATH,self.menuItem_entityManagement_Xpath).click()

    # Hospital & Safety
    def Submenu_HS(self):
        self.driver.find_element(By.XPATH,self.submenu_HS_Xpath).click()
    def Add_HS(self):
        self.driver.find_element(By.XPATH,self.add_HS_Xpath).click()
    def HS_MedicalCenter(self,P_Hospital,C_Code,phone,address):
        self.driver.find_element(By.XPATH,self.input_HS_hospital_Xpath).send_keys(P_Hospital)
        element = self.driver.find_element(By.XPATH, self.dd_HS_mobileNumber_Xpath)
        element2 = self.driver.find_element(By.XPATH, self.dd_HS_select_mobile_countryCode_Xpath)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(C_Code)
        actions.send_keys(Keys.ENTER)
        actions.move_to_element(element2).perform()
        self.driver.find_element(By.XPATH,self.input_HS_phoneNumber_Xpath).send_keys(phone)
        self.driver.find_element(By.XPATH,self.input_HS_address_Xpath).send_keys(address)
        self.driver.find_element(By.XPATH,self.btn_HS_add_Xpath).click()
        time.sleep(2)
        self.Message = self.driver.find_element(By.XPATH, "(//div[@class='toastr-text'])[1]").text
        print(self.Message)
        # time.sleep(2)
        if "Success" in self.Message:
            assert True
        else:
            print("Medical Center not Created")
            assert False
    #DNO
    def Submenu_DNO(self):
        self.driver.find_element(By.XPATH,self.submenu_DNO_Xpath).click()
    def Add_DNO(self):
        self.driver.find_element(By.XPATH, self.add_DNO_Xpath).click()
    def DNO(self,DNO):
        self.driver.find_element(By.XPATH,self.input_DNO_Xpath).send_keys(DNO)
        self.driver.find_element(By.XPATH,self.btn_DNO_add_Xpath).click()
        self.Message = self.driver.find_element(By.XPATH, "(//div[@class='toastr-text'])[1]").text
        print(self.Message)
        # time.sleep(2)
        if "Success" in self.Message:
            assert True
        else:
            print("SLA not Created")
            assert False

    #SLA
    def Submenu_SLA(self):
        self.driver.find_element(By.XPATH,self.submenu_SLA_Xpath).click()
    def Add_SLA(self):
        self.driver.find_element(By.XPATH,self.add_SLA_Xpath).click()
    def SLA(self,Level,description):
        self.driver.find_element(By.XPATH,self.input_SLA_Level_Xpath).send_keys(Level)
        self.driver.find_element(By.XPATH, self.input_SLA_Description_Xpath).send_keys(description)
        self.driver.find_element(By.XPATH,self.btn_add_SLA_Xpath).click()
        self.Message = self.driver.find_element(By.XPATH, "(//div[@class='toastr-text'])[1]").text
        print(self.Message)
        # time.sleep(2)
        if "Success" in self.Message:
            assert True
        else:
            print("SLA not Created")
            assert False



