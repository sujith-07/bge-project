import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

class client:
    menuitem_client_Xpath = '//a[@href="/clients"]'
    btn_addClient_class ='nk-block-tools-opt'
    btn_back_linkText = 'Back'
    input_name_Xpath = '//input[@name="name"]'
    dd_phoneNumber_class = "p-0.col-4.col-md-2.col-lg-3"
    dd_select_phoneNumber_Class ="css-1g6gooi"
    input_phoneNumber_Xpath = '//input[@name="phoneNumber"]'
    input_addressline1_Xpath = '//input[@name="addressLine1"]'
    dd_mobileNumber_Xpath = "//div[contains(@class,'form-control-wrap d-flex')]//div[contains(@class,'p-0 col-4 col-md-2 col-lg-3')]"
    dd_select_mobile_countryCode_Xpath = "//div[contains(@class,'form-control-wrap d-flex')]//div[contains(@class,'css-1g6gooi')]"
    input_mobileNumber_xpath = '//input[@name="mobileNumber"]'
    input_email_Xpath = '//input[@name="email"]'
    input_city_Xpath = '//input[@name="city"]'
    input_postalcode_Xpath = '//input[@name="postalCode"]'
    input_website_Xpath = '//input[@name="website"]'
    dd_TaskVisibility_option_Class = '[contains(text(), '"+status+"')]'
    dd_TaskVisibility_Xpath= '(//div[@class="react-select-container css-2b097c-container"])[3]'
    btn_addPlant_Xpath = "//span[normalize-space()='Add Plant']"
    input_addplant_PlantName_Xpath='(//input[@name="name"])[2]'
    input_addplant_Size_Xpath = '//input[@name="size"]'
    input_addPlant_Acronym_Xpath='//input[@name="identifier"]'
    input_addPlant_onBoardingDate_Xpath = '//input[@class="form-control date-picker react-datepicker-ignore-onclickoutside"]'
    DD_addPlant_Status_Xpath = "(//div[contains(@class,'react-select__control css-yk16xz-control')])[4]"
    btn_addPant_AddPlant='//button[text()="Add Plant"]'
    btn_addUser_Xpath = "//span[normalize-space()='Add User']"
    input_addUser_firstName_Xpath= "//input[@name='firstName']"
    input_addUser_lastName_Xpath = "//input[@name='lastName']"
    input_addUser_Email_Xpath = "//input[@type='email']"
    input_addUser_Password_Xpath = "//input[@name='password']"
    btn_addUser_AddUser_Xpath = "//button[contains(text(),'Add User')]"
    btn_createClient_Xpath = "//button[normalize-space()='Create Client']"

    #Client List Page
    search_bar_Xpath = "(//em[@class='icon ni ni-search'])[2]"
    # input_search_Xpath = "(//input[@placeholder='Search by user or email'])[1]"
    input_search_Xpath = '//input[@class="border-transparent form-focus-none form-control"]'
    search_icon_Xpath = "(//em[@class='icon ni ni-search'])[3]"



    def __init__(self,driver):
         self.driver = driver
    def client_menu(self):
        self.driver.find_element(By.XPATH,self.menuitem_client_Xpath).click()
    def addClient(self):
        self.driver.find_element(By.CLASS_NAME,self.btn_addClient_class).click()
    def back(self):
        self.driver.find_element(By.LINK_TEXT,self.btn_back_linkText).click()
    def name(self,name):
        self.driver.find_element(By.XPATH,self.input_name_Xpath).clear()
        self.driver.find_element(By.XPATH, self.input_name_Xpath).send_keys(name)
    def Phone_Country_Code(self,code):
        element = self.driver.find_element(By.CLASS_NAME,self.dd_phoneNumber_class)
        element2 = self.driver.find_element(By.CLASS_NAME, self.dd_select_phoneNumber_Class)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(code)
        actions.send_keys(Keys.ENTER)
        actions.move_to_element(element2).perform()
    def phoneNumber(self,number):
        self.driver.find_element(By.XPATH,self.input_phoneNumber_Xpath).send_keys(number)

    def Address(self,address):
        self.driver.find_element(By.XPATH,self.input_addressline1_Xpath).send_keys(address)
    def Mobile_Country_Code(self,code):
        element = self.driver.find_element(By.XPATH,self.dd_mobileNumber_Xpath)
        element2 = self.driver.find_element(By.XPATH,self.dd_select_mobile_countryCode_Xpath)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(code)
        actions.send_keys(Keys.ENTER)
        actions.move_to_element(element2).perform()
    def MobileNumber(self,number):
        self.driver.find_element(By.XPATH,self.input_mobileNumber_xpath).send_keys(number)
    def Email(self,email):
        self.driver.find_element(By.XPATH, self.input_email_Xpath).click()
        self.driver.find_element(By.XPATH,self.input_email_Xpath).send_keys(email)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
     #     print(type(email))
     #     self.email = email
     #     self.driver.find_element(By.XPATH,self.input_email_Xpath).click()
     #     self.driver.find_element(By.XPATH,self.input_email_Xpath).send_keys(self.email)
     #     # print(email)
     #     return self.email
    def City(self,city):
        self.driver.find_element(By.XPATH,self.input_city_Xpath).send_keys(city)
    def Postal_Code(self,p_code):
        self.driver.find_element(By.XPATH,self.input_postalcode_Xpath).send_keys(p_code)
    def Website(self,website):
        self.driver.find_element(By.XPATH,self.input_website_Xpath).send_keys(website)
    def Task_Visibility_Open(self,status):
         self.driver.find_element(By.XPATH,self.dd_TaskVisibility_Xpath).click()
         time.sleep(3)
         if status=='Open':
             self.driver.find_element(By.XPATH, '//div[text()="Open"]').click()
             self.driver.find_element(By.XPATH,'//label[text()="Task Visibility"]').click()
         if status=='Completed':
             self.driver.find_element(By.XPATH, '//div[text()="Completed"]').click()
             self.driver.find_element(By.XPATH, '//label[text()="Task Visibility"]').click()
         if status=='Ready for Approval':
             self.driver.find_element(By.XPATH, '//div[text()="Ready for Approval"]').click()
             self.driver.find_element(By.XPATH, '//label[text()="Task Visibility"]').click()
         if status=='In progress':
             self.driver.find_element(By.XPATH, '//div[text()="In progress"]').click()
             self.driver.find_element(By.XPATH, '//label[text()="Task Visibility"]').click()
    def Add_Plant(self):
        self.driver.find_element(By.XPATH,self.btn_addPlant_Xpath).click()
    def PlantName(self,name):
        self.driver.find_element(By.XPATH,self.input_addplant_PlantName_Xpath).send_keys(name)
    def Size(self,size):
         self.driver.find_element(By.XPATH,self.input_addplant_Size_Xpath).send_keys(size)
    def Acronym(self,acronym):
        self.driver.find_element(By.XPATH,self.input_addPlant_Acronym_Xpath).send_keys(acronym)
    def On_Boarding_Date(self,date):
        self.driver.find_element(By.CLASS_NAME,"react-datepicker-wrapper").click()
        self.driver.find_element(By.XPATH,self.input_addPlant_onBoardingDate_Xpath).send_keys(date)
    def Status(self,status):
        self.driver.find_element(By.XPATH,self.DD_addPlant_Status_Xpath).click()
        time.sleep(3)
        if status=='Active':
            self.driver.find_element(By.XPATH,'//div[text()="Active"]').click()
        if status=='In Active':
            self.driver.find_element(By.XPATH,'//div[text()="In Active"]').click()
        if status=='Suspended':
            self.driver.find_element(By.XPATH,'//div[text()="Suspended"]').click()
    def AddPlant(self):
        self.driver.find_element(By.XPATH,self.btn_addPant_AddPlant).click()
        time.sleep(3)
    def plant_tableData(self,name):
        element = self.driver.find_element(By.XPATH,"(//div[contains(@class,'user-name')])[2]").text
        if element== name:
            print("True")
            print(name)
            assert True
        else:
            print("False")
    def Add_User(self):
        self.driver.find_element(By.XPATH,self.btn_addUser_Xpath).click()
    def First_name(self,name):
        self.driver.find_element(By.XPATH,self.input_addUser_firstName_Xpath).send_keys(name)
    def Last_name(self, name):
        self.driver.find_element(By.XPATH, self.input_addUser_lastName_Xpath).send_keys(name)
    def email(self,mail):
        self.driver.find_element(By.XPATH, self.input_addUser_Email_Xpath).send_keys(mail)
    def Password(self,password):
        self.driver.find_element(By.XPATH, self.input_addUser_Password_Xpath).send_keys(password)
    def AddUser(self):
        self.driver.find_element(By.XPATH,self.btn_addUser_AddUser_Xpath).click()
    def clientUser_tableData(self,email):
       element=self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[13]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]").text
       if element==email:
           print("True")
           # print(email)
           assert True
       else:
           print("fail")
           assert False
    def createClient(self):
        self.driver.find_element(By.XPATH,self.btn_createClient_Xpath).click()
    def search_client(self,email):
        # print(self.Email(self.email))
        print("AAAAAAAAAAAAAAAAAA")
        self.driver.find_element(By.XPATH,self.search_bar_Xpath).click()
        self.a = self.driver.find_element(By.XPATH, self.input_search_Xpath)
        self.driver.execute_script("arguments[0].value = arguments[1]", self.a, email)
        self.driver.find_element(By.XPATH, self.search_icon_Xpath).click()
        time.sleep(6)
        # actions = ActionChains(self.driver)
        # actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, self.search_icon_Xpath).click()
        # time.sleep(3)
        # self.split_email = email.split("@")[0]
        # self.after_email = email.split("@")[1]
        # print(self.after_email)
        # self.list = []
        # self.list.append(email)
        # self.driver.find_element(By.XPATH, self.search_bar_Xpath).click()
        # self.driver.find_element(By.XPATH, self.input_search_Xpath).setAttribute("name", "email")
        # time.sleep(2)
        # # self.driver.execute_script("document.getElementByClass('border-transparent form-focus-none form-control').setAttribute('value', email)")
        # self.driver.find_element(By.XPATH, self.input_search_Xpath).clear()
        # # for i in email:
        # self.driver.find_element(By.XPATH, self.input_search_Xpath).send_keys('{split_email}@'.format(split_email=self.split_email))
        # self.driver.find_element(By.XPATH, self.search_icon_Xpath).click()
        # time.sleep(6)

        # # self.driver.find_element(By.XPATH,'//input[@class="form-control border-transparent form-focus-none"]').click()
        # # self.driver.find_element(By.XPATH,'//input[@class="form-control border-transparent form-focus-none"]').send_keys()
        # print(email)
        #



























