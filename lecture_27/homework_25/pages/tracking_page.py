from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TrackingPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"
        self.tracking_input_locator = (By.CSS_SELECTOR, "input[type='text']")
        self.status_text_locator = (By.CSS_SELECTOR, "div.header__status-text")

    def open(self):
        self.driver.get(self.url)

    def enter_tracking_number(self, tracking_number):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.tracking_input_locator)
        )
        input_field.clear()
        input_field.send_keys(tracking_number)
        input_field.send_keys(Keys.RETURN)

    def get_status_text(self):
        status_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.status_text_locator)
        ).text
        return status_text
