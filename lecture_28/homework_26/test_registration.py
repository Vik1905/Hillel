def test_google_search_with_cookies(driver, open_start_page, click_sign_in, fill_in_registration_form,
                                    click_registration, check_link_after_registration):
    open_start_page()
    click_sign_in()
    fill_in_registration_form()
    click_registration()
    check_link_after_registration()
