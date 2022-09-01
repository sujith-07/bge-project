import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class settings:
    #User Management
    menuitem_settings_xpath="//span[normalize-space()='Settings']"
    submenuitem_userManagement_xpath="//span[normalize-space()='User Management']"
    add_user_xpath="//em[@class='icon ni ni-plus']"
    input_user_firstname_xpath="//input[@name='firstName']"
    input_user_lastname_xpath="//input[@name='lastName']"
    input_user_email_xpath="//input[@name='email']"
    dd_phoneNumber_class = "p-0.col-4.col-md-2.col-lg-3"
    dd_select_phoneNumber_Class ="css-1g6gooi"
    input_user_phoneNumber_Xpath = '//input[@name="phoneNumber"]'
    dd_mobileNumber_Xpath = "(//div[contains(@class,'form-control-wrap d-flex')]//div[contains(@class,'p-0 col-4 col-md-2 col-lg-3')])[2]"
    dd_select_mobile_countryCode_Xpath = "//div[contains(@class,'form-control-wrap d-flex')]//div[contains(@class,'css-1g6gooi')]"
    input_user_mobileNumber_xpath = '//input[@name="mobileNumber"]'
    input_user_password_xpath="//input[@name='password']"
    inputDD_status_xpath = "(//div[contains(text(),'Select')])[1]"
    inputDD_userRole_xpath="(//div)[117]"
    btn_createUser_xpath="//button[normalize-space()='Create User']"

    #Roles
    submenuitem_roles_xpath="//a[@href='/role_management']"
    add_roles_xpath = "//em[@class='icon ni ni-plus']"
    input_role_name_xpath="//input[@name='name']"
    DD_role_level_xpath="(//div[@class='react-select__value-container css-1hwfws3'])[1]"
    btn_add_role_xpath="//button[normalize-space()='Add']"


    #Roles
    def __init__(self,driver):
        self.driver=driver

    def Menu_Settings(self):
        self.driver.find_element(By.XPATH, self.menuitem_settings_xpath).click()
    def Submenu_Roles(self):
        self.driver.find_element(By.XPATH,self.submenuitem_roles_xpath).click()
    def add_roles(self):
        self.driver.find_element(By.XPATH,self.add_roles_xpath).click()
    def name(self,name):
        self.driver.find_element(By.XPATH,self.input_role_name_xpath).send_keys(name)
    def level(self,level):
        self.driver.find_element(By.XPATH,self.DD_role_level_xpath).click()
        self.driver.find_element(By.XPATH,'//div[contains(text(),"'+level+'")]').click()
    def Actions(self,actions):
        if actions=="Plant":
            self.driver.find_element(By.XPATH,"(//input[contains(@type,'checkbox')])[6]").click()
        elif actions=="User":
            self.driver.find_element(By.XPATH,"(//input[contains(@type,'checkbox')])[1]").click()
        elif actions=="Client":
            self.driver.find_element(By.XPATH,"(//input[contains(@type,'checkbox')])[11]").click()
        elif actions=="Asset":
            self.driver.find_element(By.XPATH,"(//input[contains(@type,'checkbox')])[16]").click()
        elif actions=="Asset Category":
            self.driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[19]").click()
        elif actions=="Manufacturer":
            self.driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[22]").click()
        elif actions=="Sla":
            self.driver.find_element(By.XPATH,"(//input[contains(@type,'checkbox')])[25]").click()
        elif actions=="Home and Safety":
            self.driver.find_element(By.XPATH,"(//input[contains(@type,'checkbox')])[28]").click()
        elif actions=="Dno":
            self.driver.find_element(By.XPATH,"(//input[contains(@type,'checkbox')])[31]").click()
        elif actions=="Ticket":
            self.driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[34]").click()
        elif actions=="Role":
            self.driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[37]").click()
        elif actions=="Form":
            self.driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[40]").click()
        elif actions=="Inventory":
            self.driver.find_element(By.XPATH,"(//input[contains(@type,'checkbox')])[43]").click()
        else:
            print("No Actions Found")
    def add_role(self):
        self.driver.find_element(By.XPATH,self.btn_add_role_xpath).click()



  #User Management
    def Submenu_userManagement(self):
        self.driver.find_element(By.XPATH,self.submenuitem_userManagement_xpath).click()
    def Add_User(self):
        self.driver.find_element(By.XPATH,self.add_user_xpath).click()
    def firstname(self,f_name):
        self.driver.find_element(By.XPATH,self.input_user_firstname_xpath).send_keys(f_name)
    def lastname(self,l_name):
        self.driver.find_element(By.XPATH,self.input_user_lastname_xpath).send_keys(l_name)
    def Email(self,email):
        self.driver.find_element(By.XPATH,self.input_user_email_xpath).send_keys(email)
    def Phone_Country_Code(self,code):
        element = self.driver.find_element(By.CLASS_NAME,self.dd_phoneNumber_class)
        element2 = self.driver.find_element(By.CLASS_NAME, self.dd_select_phoneNumber_Class)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(code)
        actions.send_keys(Keys.ENTER)
        actions.move_to_element(element2).perform()
    def phoneNumber(self,number):
        self.driver.find_element(By.XPATH,self.input_user_phoneNumber_Xpath).send_keys(number)
    def Mobile_Country_Code(self,code):
        element = self.driver.find_element(By.XPATH,self.dd_mobileNumber_Xpath)
        element2 = self.driver.find_element(By.XPATH,self.dd_select_mobile_countryCode_Xpath)
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.send_keys(code)
        actions.send_keys(Keys.ENTER)
        actions.move_to_element(element2).perform()
    def MobileNumber(self,number):
        self.driver.find_element(By.XPATH,self.input_user_mobileNumber_xpath).send_keys(number)
    def Password(self,password):
        self.driver.find_element(By.XPATH,self.input_user_password_xpath).send_keys(password)
    def Status(self,status):
        self.driver.find_element(By.XPATH, self.inputDD_status_xpath).click()
        time.sleep(3)
        if status == 'ACTIVE':
            self.driver.find_element(By.XPATH, '//div[text()="ACTIVE"]').click()
        if status == 'INACTIVE':
            self.driver.find_element(By.XPATH, '//div[text()="INACTIVE"]').click()
        if status == 'SUSPENDED':
            self.driver.find_element(By.XPATH, '//div[text()="SUSPENDED"]').click()
    def User_Role(self,role):
        self.driver.find_element(By.XPATH,self.inputDD_userRole_xpath).click()
        self.driver.find_element(By.XPATH,'//div[contains(text(),"'+role+'")]').click()
        self.driver.find_element(By.XPATH,"//label[@for='roleIds']").click()
    def CreateUser(self):
        self.driver.find_element(By.XPATH,self.btn_createUser_xpath).click()
        time.sleep(2)
        self.Message = self.driver.find_element(By.XPATH, "(//div[@class='toastr-text'])[1]").text
        print(self.Message)
        # time.sleep(2)
        if "Success" in self.Message:
            assert True
        else:
            print("DNO not Created")
            assert False