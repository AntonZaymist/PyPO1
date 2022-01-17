from page_object.main_page import MainPage


def test_main_page(chrome_driver):
    page = MainPage(chrome_driver)
    page.open()
    login_page = page.open_login_page()
    assert login_page.get_login_form().is_displayed(), "Login form doesn't exists"
    assert 'Login' in login_page.get_title(), "Title doesn't contain Login"


def test_login(chrome_driver):
    page = MainPage(chrome_driver)
    page.open()
    login_page = page.open_login_page()
    login_page.try_to_login()
    assert login_page.get_oops(), "Oops message doesn't exist"

