from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyAccountPage:
    lnk_logout_xpath = "//*[@id='top']//a[text()='Logout']"
    btn_continue_xpath = "//a[@class='btn btn-primary' and text()='Continue']"
    def __init__(self, driver):
        self.driver = driver
    def click_logout(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.lnk_logout_xpath))).click()
    def click_continue(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.btn_continue_xpath))).click()