from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.readproperty import ReadConfig
class LoginPage:
    txt_login_email_xpath="//input[@id='input-email']"
    txt_login_password_xpath="//input[@id='input-password']"
    btn_login_xpath="//button[text()='Login']"
    msg_myaccount_xpath="//h1[normalize-space()='My Account']"
    def __init__(self, driver):
        self.driver=driver
    def enter_email(self,email):
        self.driver.find_element(By.XPATH,self.txt_login_email_xpath).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.txt_login_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def ismyaccountPageExist(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.msg_myaccount_xpath)
                )
            )
            return True
        except:
            return False