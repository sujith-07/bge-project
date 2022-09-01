import time

import pytest
from faker import Faker

from pageObjects.Settings import settings
from pageObjects.login_Module import Login

@pytest.mark.usefixtures("init__driver")
class Test_Settings:
    def test_settings(self):
        self.lp=Login(self.driver)
        self.lp.email("bge01@yopmail.com")
        self.lp.password("qwerty123")
        self.lp.login()
        faker= Faker()
        self.settings=settings(self.driver)
        self.settings.Menu_Settings()
        self.settings.Submenu_Roles()
        self.settings.add_roles()
        self.settings.name("Super admin 12")
        self.settings.level("Admin")
        self.settings.Actions("Plant")
        self.settings.add_role()
        time.sleep(3)
        self.settings.Menu_Settings()
        self.settings.Submenu_userManagement()
        self.settings.Add_User()
        self.settings.firstname(faker.first_name())
        self.settings.lastname(faker.last_name())
        self.settings.Email(faker.email())
        self.settings.Phone_Country_Code("+91")
        self.settings.phoneNumber(faker.msisdn())
        self.settings.Mobile_Country_Code("+93")
        self.settings.MobileNumber(faker.msisdn())
        self.settings.Password("test@123")
        self.settings.Status("ACTIVE")
        self.settings.User_Role("Admin")
        #time.sleep(2)
        self.settings.User_Role("System Admin")
        #time.sleep(3)
        self.settings.CreateUser()


