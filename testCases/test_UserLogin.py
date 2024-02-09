import time

from selenium import webdriver
import pytest
from utilities.Logger import LoggenClass
from pageObjects.LoginPage import LoginClass
from utilities.readconfigfile import Readconfig


class Test_Login:
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    log=LoggenClass.log_generator()

    def test_verify_url_001(self, setup):
        self.log.info("Test_Case test_verify_url_001 is started")
        self.driver = setup
        self.log.info("opening browser and nevigating to demo_nop_com")
        self.log.info("page title is-->" +self.driver.title)
        #print(self.driver.title)
        if self.driver.title == "Your store. Login":
            self.log.info("Test_Case test_verify_url_001 is passed")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url_001_pass.png")
            assert True
        else:
            self.log.info("Test_Case test_verify_url_001 is failed")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url_001_fail.png")
            assert False
        self.log.info("Test_case test_verify_url_001 is completed")

    @pytest.mark.sanity
    def test_user_login_002(self, setup):
        self.log.info("Test_case test_user_login_002 is started")
        self.driver = setup
        self.log.info("opening browser and nevigating to demo_nop_com")
        self.lp = LoginClass(self.driver)
        self.log.info("Entering email-" +self.Email)
        self.lp.Enter_Email(self.Email)
        self.log.info("Entering password-" +self.Password)
        self.lp.Enter_Password(self.Password)
        self.log.info("Click on login button")
        self.lp.Click_Login()
        if self.lp.Verify_Login_Stauts() == "Login Pass":
            self.log.info("Test_Case test_user_login_002 is passes")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_pass.png")
            self.log.info("click on logout button")
            self.lp.Click_Logout()
            assert True
        else:
            self.log.info("Test_Case test_user_login_002 is failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_fail.png")
            assert False
        self.log.info("Test_Case test_user_login_002 is completed")

# pytest -v -n=2 --html=HtmlReports/myreport.html\

# test_emp_add
# test_emp_edit
# test_emp_search
#
# -k test_emp
