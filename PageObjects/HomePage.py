from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    lnk_myaccount_xpath = "//*[@id='top']/div/div/div[2]/ul/li[2]/div/a/span"
    lnk_registeraccount_xpath = "//a[normalize-space()='Register']"
    lnk_loginaccount_xpath = "//a[normalize-space()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def click_myaccount(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.lnk_myaccount_xpath))
        ).click()

    def click_registeraccount(self):
        # First open My Account dropdown
        self.click_myaccount()
        # Then wait for Register link to be visible
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lnk_registeraccount_xpath))
        ).click()

    def click_loginaccount(self):
        self.click_myaccount()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lnk_loginaccount_xpath))
        ).click()
