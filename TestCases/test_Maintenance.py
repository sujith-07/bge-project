import time

import pytest

from BGE_Project.pageObjects.Maintenance import Maintenance
from BGE_Project.pageObjects.login_Module import Login


@pytest.mark.usefixtures("init__driver")
class Test_maintenance:
    def test_correctiveMaintenance(self):
        self.lp = Login(self.driver)
        self.lp.email("bge01@yopmail.com")
        self.lp.password("qwerty123")
        self.lp.login()
        self.cm=Maintenance(self.driver)
        self.cm.Maintenance()
        self.cm.correctiveMaintenance()
        time.sleep(3)
        self.cm.add_CorrectiveMaintenance()
        self.cm.taskName("Test123")
        self.cm.priority("High")
        #time.sleep(3)
        self.cm.SLA("Myron Conn I")
        self.cm.status("Open")
        self.cm.plantName("Elijah Buckridge")
        self.cm.fieldEngineer("BGE 02")
        self.cm.startDate()
        #time.sleep(2)
        self.cm.assignedTo("BGE 01")
        time.sleep(2)
        self.cm.resolvedDate()
        time.sleep(2)
        self.cm.assetCategory("AssetCategory2")
        self.cm.description("Task Added")
        self.cm.relatedTask("testname")
        self.cm.add_maintanance()
        #time.sleep(3)

