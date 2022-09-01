import time

import pytest
from selenium.webdriver.common.by import By




from faker import Faker

from BGE_Project.pageObjects.Client_Module import client
from BGE_Project.pageObjects.login_Module import Login


@pytest.mark.usefixtures("init__driver")
class Test_client_module:
    def test_client(self):
        self.lp = Login(self.driver)
        self.lp.email("bge01@yopmail.com")
        self.lp.password("qwerty123")
        self.lp.login()
        self.client = client(self.driver)
        self.client.client_menu()
        self.client.addClient()
        faker = Faker()
        self.emails = faker.email()

        self.client.name(faker.name())
        #time.sleep(5)
        self.client.Phone_Country_Code("+91")
        #time.sleep(10)
        self.client.phoneNumber(faker.msisdn())
        self.client.Address("Korea")
        #time.sleep(3)
        self.client.Mobile_Country_Code("+376")
        #time.sleep(3)
        self.client.MobileNumber(faker.msisdn())
        #time.sleep(3)
        self.client.Email(self.emails)
        self.client.City(faker.country())
        self.client.Postal_Code(faker.postcode())

        self.client.Website("https://google.com")
        #time.sleep(3)
        self.client.Task_Visibility_Open("Open")
        #time.sleep(3)
        self.client.Task_Visibility_Open("In Progress")
        #time.sleep(3)
        # self.client.Task_Visibility_Open("In Progress")
        # time.sleep(3)
        # self.client.Add_Plant()
        # self.client.PlantName("Virat")
        # self.client.Size("200")
        # self.client.Acronym("CDEF")
        # self.client.On_Boarding_Date("21/08/2022")
        # self.client.Status("In Active")
        # self.client.AddPlant()
        # time.sleep(3)
        # self.client.plant_tableData("Virat")
        # time.sleep(3)
        # self.client.Add_User()
        # self.client.First_name("Kohli")
        # self.client.Last_name("ABCD")
        # self.client.email("Kohli98@yopmail.com")
        # self.client.Password("test@1234")
        # self.client.AddUser()
        # time.sleep(3)
        # self.client.clientUser_tableData("Kohli98@yopmail.com")
        # time.sleep(3)
        self.client.createClient()
        time.sleep(3)
        # self.client.driver.back()
        self.msg=self.driver.find_element(By.XPATH,"(//div[contains(@class,'toastr-text')])[1]").text
        print(self.msg)
        if "Client created successfully" in self.msg:
            #print("Client Created Successfully")
            assert True == True
        else:
            print("fail")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addClient.png")
            assert True == False

        time.sleep(5)
        self.client.search_client(self.emails)











