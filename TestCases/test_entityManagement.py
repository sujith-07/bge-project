import time

import pytest

from BGE_Project.pageObjects.Entity_Management import Entity_Management
from BGE_Project.pageObjects.login_Module import Login


@pytest.mark.usefixtures("init__driver")
class Test_entityManagement:
    def test_healthAndSafety(self):
        self.lp = Login(self.driver)
        self.lp = Login(self.driver)
        self.lp.email("bge01@yopmail.com")
        self.lp.password("qwerty123")
        self.lp.login()
        self.entity = Entity_Management(self.driver)
        self.entity.Menu_EntityManagement()
        self.entity.Submenu_HS()
        self.entity.Add_HS()
        self.entity.HS_MedicalCenter("TestHospital","+144","98765432154","TestAddress")
        time.sleep(3)
        #DNO
        self.entity.Submenu_DNO()
        self.entity.Add_DNO()
        self.entity.DNO("user338")
        time.sleep(3)
        #SLA
        self.entity.Submenu_SLA()
        self.entity.Add_SLA()
        self.entity.SLA("Level8","SLA Level10")

