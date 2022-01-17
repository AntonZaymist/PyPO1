from page_object.base_page import BasePage
from page_object.books_page_locators import BooksPageLocators
from page_object.search_page import SearchPage


class BooksPage(BasePage):

    def get_header(self):
        return self.find_element(BooksPageLocators.HEADER_LOCATORS)

    def get_site_tree(self):
        return self.find_element(BooksPageLocators.SITE_TREE_LOCATORS)

    def open_search_book(self, book_name):
        input_search = self.find_element(BooksPageLocators.INPUT_SEARCH_LOCATORS)
        input_search.send_keys(book_name)
        # input_search.submit()
        button = self.find_element(BooksPageLocators.BUTTON_SEARCH_LOCATORS)
        button.click()
        return SearchPage(self.chrome_driver, self.chrome_driver.current_url)
