from PageObjects.HomePage import HomePage
from PageObjects.RegisterPage import RegisterPage
from Utitlities.random_string import random_string
from Utitlities.readproperty import ReadConfig
import os
import pytest
from Utitlities.customlogger import LogGen
class TestRegisterPage:
    base_url=ReadConfig.get_application_url()
    firstname=ReadConfig.get_firstname()
    lastname=ReadConfig.get_lastname()
    password=ReadConfig.set_password()
    logger=LogGen.logging()
    #Warn>Debug>info>error>fatal
    @pytest.mark.regression
    def test_account_registration(self,setup):
        self.logger.info("account_registration is started")
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.hp=HomePage(self.driver)
        self.hp.click_registeraccount()
        self.rp=RegisterPage(self.driver)
        self.rp.Set_firstname(self.firstname)
        self.rp.Set_lastname(self.lastname)
        self.unique_email = f"{random_string()}@gmail.com"
        self.rp.Set_email(self.unique_email)
        self.rp.Set_password(self.password)
        self.rp.Click_subscribe()
        self.rp.Click_privacy_policy()
        self.rp.Click_continue()
        # self.driver.save_screenshot("after_continue.png")
        self.confirmsg=self.rp.Register_confirmation()
        if self.confirmsg=="Your Account Has Been Created!":
            self.logger.info("Account Registration Successful")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\Screenshots\\"+"test_account_reg.png")
            self.logger.error("Account Registration Failed")
            self.driver.close()
            assert False