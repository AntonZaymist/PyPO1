from page_object.base_page import BasePage
from page_object.search_page_locators import SearchPageLocators


class SearchPage(BasePage):

    def open_image_book(self):
        image_book = self.find_element(SearchPageLocators.BOOK_IMAGE_LOCATORS)
        image_book.click()

    def get_title(self):
        return self.chrome_driver.title
