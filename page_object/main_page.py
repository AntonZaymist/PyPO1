from page_object.base_page import BasePage
from page_object.books_page import BooksPage
from page_object.login_page import LoginPage
from page_object.main_page_locators import MainPageLocators


class MainPage(BasePage):
    URL = 'http://selenium1py.pythonanywhere.com/en-gb/'

    def __init__(self, chrome_driver):
        super().__init__(chrome_driver, self.URL)

    def open_login_page(self):
        login_link = self.find_element(MainPageLocators.LOGIN_LINK_LOCATORS)
        login_link.click()
        return LoginPage(self.chrome_driver, self.chrome_driver.current_url)

    def open_books_page(self):
        books_link = self.find_element(MainPageLocators.BOOKS_REF_LOCATORS)
        books_link.click()
        return BooksPage(self.chrome_driver, self.chrome_driver.current_url)
