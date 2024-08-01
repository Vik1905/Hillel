import allure

@allure.feature('Регистрация')
def test_registration(driver, open_start_page, click_sign_in, fill_in_registration_form, click_registration, check_link_after_registration):
    with allure.step("Открытие стартовой страницы"):
        open_start_page()
    with allure.step("Нажатие на кнопку 'Sign In'"):
        click_sign_in()
    with allure.step("Заполнение регистрационной формы"):
        fill_in_registration_form()
    with allure.step("Нажатие на кнопку 'Register'"):
        click_registration()
    with allure.step("Проверка ссылки после регистрации"):
        check_link_after_registration()
