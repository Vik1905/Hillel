import pytest
from selenium import webdriver
from lecture_27.homework_24.pages.tracking_page import TrackingPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_tracking_status(driver):
    tracking_page = TrackingPage(driver)
    tracking_page.open()

    tracking_number = "59001185450754"
    expected_status = "Отримана"

    tracking_page.enter_tracking_number(tracking_number)
    status_text = tracking_page.get_status_text()

    assert status_text == expected_status, f"Expected '{expected_status}', but got '{status_text}'"

if __name__ == "__main__":
    pytest.main()
