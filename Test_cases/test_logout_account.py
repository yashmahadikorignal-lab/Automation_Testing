import pytest
import time
from Utilities.readproperty import ReadConfig
from Utilities.XLutils import ExcelUtils
from Utilities.customlogger import LogGen
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.RegisterPage import RegisterPage
from PageObjects.MyAccountPage import MyAccountPage
import os
class Test_Login:
    baseurl=ReadConfig.get_application_url()
    logger=LogGen.logging()
    path=os.path.abspath(os.curdir)+"\\Test_Data\\Opencart_Login_Data.xlsx"
    @pytest.mark.regression
    def test_login_dtt(self,setup):
        self.xl=ExcelUtils(file_path=self.path)
        self.logger.info("Starting test_login_dtt")
        self.rows=self.xl.get_total_rows('Sheet1')
        lst_status=[]
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.hp=HomePage(self.driver)
        self.lp=LoginPage(self.driver)
        self.ac=MyAccountPage(self.driver)
        for r in range(2,self.rows+1):
            self.hp.click_loginaccount()
            self.email=self.xl.read_cell('Sheet1',r,1)
            self.password=self.xl.read_cell('Sheet1',r,2)
            self.exp=self.xl.read_cell('Sheet1',r,3)
            self.lp.enter_email(self.email)
            self.lp.enter_password(self.password)
            self.lp.click_login()
            self.driver.implicitly_wait(10)
            self.targetpage=self.lp.ismyaccountPageExist()
            if self.exp=='Valid':
                if self.targetpage==True:
                    lst_status.append("pass")
                    self.hp.click_myaccount()
                    self.ac.click_logout()
                    self.ac.click_continue()
                else:
                    lst_status.append("fail")
            elif self.exp=='Invalid':
                if self.targetpage==True:
                    lst_status.append("fail")
                    self.hp.click_myaccount()
                    self.ac.click_logout()
                    self.ac.click_continue()
                else:
                    lst_status.append("pass")
        self.driver.close()
        if "fail" not in lst_status:
            assert True
        else:
            self.logger.info("end test_login_dtt")
            assert False




