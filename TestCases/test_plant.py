import time

import pytest

from pageObjects.PV_Plant import plant
from pageObjects.login_Module import Login

@pytest.mark.usefixtures("init__driver")
class Test_Plant_Module:
    def test_plant(self):
        self.lp = Login(self.driver)
        self.lp.email("bge01@yopmail.com")
        self.lp.password("qwerty123")
        self.lp.login()
        self.plant=plant(self.driver)
        self.plant.MenuItem_PvPlant()
        self.plant.Add_Plant()
        self.plant.Plant_Name("test plant")
        self.plant.Plant_Size("123")
        self.plant.Plant_Acronym("test123")
        self.plant.Plant_OnBoardingDate("2022-08-21")
        self.plant.Plant_ClientName("William Bailey")
        self.plant.Plant_PlantManager("Deepak ABC")
        self.plant.Plant_TeamLeader("BGE 02")
        self.plant.Plant_FieldEngineer("BGE 03")
        self.plant.Plant_Status("ACTIVE")
        self.plant.Plant_PostalCode("123456")
        self.plant.Plant_Address("New York")
        self.plant.Plant_GoogleMapLink("WWW.google.com")
        self.plant.Plant_What3WordLink("///conquest.poets.chestnuts")
        self.plant.Plant_DNO("User334")
        time.sleep(2)
        self.plant.Plant_Hospital("Hospital","+91","94386456543","USA")
        self.plant.Plant_CreatePlant()
        time.sleep(3)

