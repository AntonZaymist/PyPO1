import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_object.main_page import MainPage


@pytest.fixture(scope="session")
def chrome_driver():
    chrome_driver = Chrome()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope="module")
def main_page(chrome_driver):
    page = MainPage(chrome_driver)
    page.open()
    return page

# @pytest.fixture(scope="session")
# def hw22_driver(chrome_driver):
#     chrome_driver.get("http://selenium1py.pythonanywhere.com/en-gb/")
#     yield chrome_driver
#     chrome_driver.close()
