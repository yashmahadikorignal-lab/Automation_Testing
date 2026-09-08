from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class RegisterPage:
    txt_first_name_xpath = "//input[@id='input-firstname']"
    txt_last_name_xpath="//input[@id='input-lastname']"
    txt_email_xpath="//input[@id='input-email']"
    txt_password_xpath="//input[@id='input-password']"
    btn_subscribe_xpath="//input[@id='input-newsletter']"
    btn_continue_xpath="//button[normalize-space()='Continue']"
    btn_privacy_policy_xpath="//input[@name='agree']"
    txt_confirmationmsg_xpath="//*[@id='common-success']/ul/li[3]/a"

    def __init__(self,driver):
        self.driver = driver

    def Set_firstname(self,firstname):
        self.driver.find_element(By.XPATH,self.txt_first_name_xpath).send_keys(firstname)

    def Set_lastname(self,lastname):
        self.driver.find_element(By.XPATH,self.txt_last_name_xpath).send_keys(lastname)

    def Set_email(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def Set_password(self,password):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(password)

    def Click_subscribe(self):
        self.driver.find_element(By.XPATH,self.btn_subscribe_xpath).click()

    def Click_privacy_policy(self):
        self.driver.find_element(By.XPATH,self.btn_privacy_policy_xpath).click()

    def Click_continue(self):
        self.driver.find_element(By.XPATH,self.btn_continue_xpath).click()

    def Register_confirmation(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.txt_confirmationmsg_xpath))
            )
            return element.text  # <-- return text, not WebElement
        except:
            return None
