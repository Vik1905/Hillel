import pytest
from selenium import webdriver
from lecture_28.homework_26.pages.home_page import HomePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def open_start_page(driver):
    def _open_start_page():
        driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    return _open_start_page


@pytest.fixture
def click_sign_in(driver):
    def _click_sign_in():
        home_page = HomePage(driver)
        home_page.click_sigh_in_button()

    return _click_sign_in


@pytest.fixture
def fill_in_registration_form(driver):
    def _fill_in_registration_form():
        home_page = HomePage(driver)
        home_page.fill_in_name_field()
        home_page.fill_in_last_name_field()
        home_page.fill_in_email_field()
        home_page.fill_in_password_field()
        home_page.fill_in_re_enter_password_field()

    return _fill_in_registration_form

@pytest.fixture
def click_registration(driver):
    def _click_registration():
        home_page = HomePage(driver)
        home_page.click_registration_button()

    return _click_registration

@pytest.fixture
def check_link_after_registration(driver):
    def _check_link_after_registration():
        home_page = HomePage(driver)
        home_page.current_url()
        assert 'https://guest:welcome2qauto@qauto.forstudy.space/panel/garage' == home_page.current_url()

    return _check_link_after_registration

