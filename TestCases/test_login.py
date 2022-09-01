import time

import pytest

from BGE_Project.Utilities.readProperties import ReadConfig
from BGE_Project.pageObjects.login_Module import Login


@pytest.mark.usefixtures("init__driver")
class Test_Admin_Login:
    baseURL = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    def test_adminLogin(self):
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.email(self.useremail)
        self.lp.password(self.password)
        self.lp.login()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "BGE Dashboard":
            assert True
        else:
            print("failed")
            assert False


