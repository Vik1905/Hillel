import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_sigh_in_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Sign up']")))
        return self.driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

    def fill_in_name_field(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='signupName']")))
        self.driver.find_element(By.XPATH, "//*[@id='signupName']").send_keys('Viktor')

    def fill_in_last_name_field(self):
        self.driver.find_element(By.XPATH, '//*[@id="signupLastName"]').send_keys("QA")

    def fill_in_email_field(self):
        self.driver.find_element(By.XPATH, '//*[@id="signupEmail"]').send_keys("Test157.593@yopmail.com")

    def fill_in_password_field(self):
        self.driver.find_element(By.XPATH, '//*[@id="signupPassword"]').send_keys("Qwerty$123")

    def fill_in_re_enter_password_field(self):
        self.driver.find_element(By.XPATH, '//*[@id="signupRepeatPassword"]').send_keys("Qwerty$123")

    def click_registration_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Register']")))
        self.driver.find_element(By.XPATH, "//button[text()='Register']").click()

    def current_url(self):
        time.sleep(5)
        return self.driver.current_url

