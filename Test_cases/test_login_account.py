import pytest
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from Utilities.customlogger import LogGen
from Utilities.readproperty import ReadConfig
import os
class TestLoginAccount:
    baseURL=ReadConfig.get_application_url()
    logger=LogGen.logging()
    email=ReadConfig.set_email()
    password=ReadConfig.set_password()
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("account logging is started")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.click_loginaccount()
        self.lg=LoginPage(self.driver)
        self.lg.enter_email(self.email)
        self.lg.enter_password(self.password)
        self.lg.click_login()
        self.driver.implicitly_wait(10)
        if self.lg.ismyaccountPageExist():
            self.logger.info("account logged in")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\Screenshots\\" + "loginfail.png")
            self.logger.error("account not logged in")
            self.driver.close()
            assert False
        # self.driver.close()
        self.logger.info("Login test ended")
        # pytest - v - s - -capture = tee-sys Test_cases / --browser = edge TO capture error in report