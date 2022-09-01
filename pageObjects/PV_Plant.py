import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


class plant:
    menuitem_pvPlant_xpath="//span[normalize-space()='PV Plants']"
    addPlant_xpath="//button[@class='btn btn-primary btn-icon']"
    input_plantName_xpath="(//input[@name='name'])[1]"
    input_size_xpath="(//input[@name='size'])[1]"
    input_acronym_xpath="(//input[@name='identifier'])[1]"
    input_onBoardingDate_xpath="//input[@class='form-control date-picker react-datepicker-ignore-onclickoutside']"
    inputDD_clientName_xpath="(//div[contains(@class,'form-control-wrap')])[5]"
    inputDD_plantManager_xpath="(//div[contains(@class,'form-control-wrap')])[6]"
    inputDD_teamLeader_xpath="(//div[contains(@class,'form-control-wrap')])[7]"
    inputDD_fieldEngineer_xpath="(//div[contains(@class,'form-control-wrap')])[8]"
    inputDD_status_xpath="//div[contains(text(),'Select the Status')]"
    input_postalCode_xpath="(//input[@name='postalCode'])[1]"
    input_address_xpath="//input[@name='address']"
    input_googleLink_xpath="//input[@name='googleMapLink']"
    input_what3WordLink_xpath="//input[@name='what3WordLink']"

    #DNO
    DD_DNO_xpath="//div[contains(text(),'Select the DNO')]"
    addDNO_xpath="(//em)[17]"
    input_addDNO_CssSelectors="div[class='col-md-12 col-lg-12'] input[name='name']"
    btn_addDNO_Xpath="(//button[normalize-space()='Add'])[1]"
    icon_close_xpath="(//em[@class='icon ni ni-cross'])[1]"


    #HOSPITAL
    inputDD_hospital_Xpath="//div[contains(text(),'Select the hospital')]"
    plus_hospital_Xpath="(//button[contains(@class,'btn btn-primary btn-icon mt-4')])[2]"
    icon_Hclose_Xpath="(//em[@class='icon ni ni-cross'])[1]"
    input_hospitalName_Xpath="(//input[contains(@name,'name')])[2]"
    dd_mobileNumber_Xpath = "//div[contains(@class,'form-control-wrap d-flex')]//div[contains(@class,'p-0 col-4 col-md-2 col-lg-3')]"
    dd_select_mobile_countryCode_Xpath = "//div[contains(@class,'form-control-wrap d-flex')]//div[contains(@class,'css-1g6gooi')]"
    input_phoneNumber_Xpath="(//input[@name='phoneNumber'])[1]"
    input_hospitalAddress_Xpath="(//input[contains(@name,'address')])[2]"
    btn_addHospital_Xpath="//button[normalize-space()='Add']"

    btn_cancel_Xpath="(//a[normalize-space()='Cancel'])[1]"
    btn_createPlant_Xpath="(//button[normalize-space()='Create Plant'])[1]"


    def __init__(self,driver):
         self.driver = driver
    def MenuItem_PvPlant(self):
        self.driver.find_element(By.XPATH,self.menuitem_pvPlant_xpath).click()
    def Add_Plant(self):
        self.driver.find_element(By.XPATH,self.addPlant_xpath).click()
    def Plant_Name(self,P_name):
        self.driver.find_element(By.XPATH,self.input_plantName_xpath).send_keys(P_name)
    def Plant_Size(self,P_size):
        self.driver.find_element(By.XPATH,self.input_size_xpath).send_keys(P_size)
    def Plant_Acronym(self,P_acronym):
        self.driver.find_element(By.XPATH,self.input_acronym_xpath).send_keys(P_acronym)
    def Plant_OnBoardingDate(self,P_date):
        self.driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker-wrapper')]").click()
        self.driver.find_element(By.XPATH,self.input_onBoardingDate_xpath).send_keys(P_date)
    def Plant_ClientName(self,C_Name):
        self.driver.find_element(By.XPATH,self.inputDD_clientName_xpath).click()
        self.driver.find_element(By.XPATH, '//div[contains(text(),"'+C_Name+'")]').click()
        #self.driver.find_element(By.XPATH, self.inputDD_clientName_xpath).send_keys(Keys.ENTER)
    def Plant_PlantManager(self,P_Managar):
        self.driver.find_element(By.XPATH, self.inputDD_plantManager_xpath).click()
        self.driver.find_element(By.XPATH, '//div[contains(text(),"'+P_Managar+'")]').click()
        #self.driver.find_element(By.XPATH, self.inputDD_plantManager_xpath).send_keys(Keys.ENTER)
    def Plant_TeamLeader(self,TL_Name):
        self.driver.find_element(By.XPATH,self.inputDD_teamLeader_xpath).click()
        self.driver.find_element(By.XPATH, '//div[contains(text(),"'+TL_Name+'")]').click()
        #self.driver.find_element(By.XPATH, self.inputDD_teamLeader_xpath).send_keys(Keys.ENTER)
    def Plant_FieldEngineer(self,FD_Name):
        self.driver.find_element(By.XPATH,self.inputDD_fieldEngineer_xpath).click()
        self.driver.find_element(By.XPATH, '//div[contains(text(),"'+FD_Name+'")]').click()
        #self.driver.find_element(By.XPATH, self.inputDD_fieldEngineer_xpath).send_keys(Keys.ENTER)
    def Plant_Status(self,status):
        self.driver.find_element(By.XPATH, self.inputDD_status_xpath).click()
        time.sleep(3)
        if status == 'ACTIVE':
            self.driver.find_element(By.XPATH, '//div[text()="ACTIVE"]').click()
        if status == 'INACTIVE':
            self.driver.find_element(By.XPATH, '//div[text()="INACTIVE"]').click()
        if status == 'SUSPENDED':
            self.driver.find_element(By.XPATH, '//div[text()="SUSPENDED"]').click()
    def Plant_PostalCode(self,code):
        self.driver.find_element(By.XPATH,self.input_postalCode_xpath).send_keys(code)
    def Plant_Address(self,P_Address):
        self.driver.find_element(By.XPATH,self.input_address_xpath).send_keys(P_Address)
    def Plant_GoogleMapLink(self,P_MapLink):
        self.driver.find_element(By.XPATH,self.input_googleLink_xpath).send_keys(P_MapLink)
    def Plant_What3WordLink(self,P_What3WordLink):
        self.driver.find_element(By.XPATH,self.input_what3WordLink_xpath).send_keys(P_What3WordLink)
    def Plant_DNO(self,P_DNO):
        self.driver.find_element(By.XPATH,self.addDNO_xpath).click()
        self.driver.find_element(By.CSS_SELECTOR, self.input_addDNO_CssSelectors).clear()
        self.driver.find_element(By.CSS_SELECTOR,self.input_addDNO_CssSelectors).send_keys(P_DNO)
        self.driver.find_element(By.XPATH,self. btn_addDNO_Xpath).click()
        time.sleep(2)
        self.Message = self.driver.find_element(By.XPATH, "(//div[@class='toastr-text'])[1]").text
        print(self.Message)
        # time.sleep(2)
        if "Success" in self.Message:
            assert True
        else:
            print("DNO not Created")
            assert False
    def Plant_Hospital(self,P_Hospital,C_Code,phone,address):
        self.driver.find_element(By.XPATH,self.plus_hospital_Xpath).click()
        self.driver.find_element(By.XPATH,self.input_hospitalName_Xpath).send_keys(P_Hospital)
        element = self.driver.find_element(By.XPATH, self.dd_mobileNumber_Xpath)
        element2 = self.driver.find_element(By.XPATH, self.dd_select_mobile_countryCode_Xpath)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(C_Code)
        actions.send_keys(Keys.ENTER)
        actions.move_to_element(element2).perform()
        self.driver.find_element(By.XPATH,self.input_phoneNumber_Xpath).send_keys(phone)
        self.driver.find_element(By.XPATH,self.input_hospitalAddress_Xpath).send_keys(address)
        self.driver.find_element(By.XPATH,self.btn_addHospital_Xpath).click()
        time.sleep(2)
        self.Message = self.driver.find_element(By.XPATH, "(//div[@class='toastr-text'])[1]").text
        print(self.Message)
        # time.sleep(2)
        if "Success" in self.Message:
            assert True
        else:
            print("DNO not Created")
            assert False

    def Plant_Cancel(self):
        self.driver.find_element(By.XPATH,self.btn_cancel_Xpath).click()
    def Plant_CreatePlant(self):
        self.driver.find_element(By.XPATH,self.btn_createPlant_Xpath).click()
        self.Message = self.driver.find_element(By.XPATH, "(//div[@class='toastr-text'])[1]").text
        print(self.Message)
        # time.sleep(2)
        if "Success" in self.Message:
            assert True
        else:
            print("DNO not Created")
            assert False