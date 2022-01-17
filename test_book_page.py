from constants import BOOK_SEARCH
from page_object.main_page import MainPage


def test_book_page(main_page):
    books_page = main_page.open_books_page()
    assert books_page.get_header().text == 'Books'


def test_search_book(chrome_driver):
    page = MainPage(chrome_driver)
    page.open()
    books_page = page.open_books_page()
    search_page = books_page.open_search_book(BOOK_SEARCH)
    search_page.open_image_book()
    assert BOOK_SEARCH in search_page.get_title()



