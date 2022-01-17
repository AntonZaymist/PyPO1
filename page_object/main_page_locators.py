from selenium import webdriver
from selenium.webdriver.common.by import By
from page_object.login_page_locators import LoginPageLocators


class MainPageLocators:
    LOGIN_LINK_LOCATORS = (By.CSS_SELECTOR, "#login_link")
    OSCAR_REF_LOCATORS = (By.CSS_SELECTOR, 'div[href="/en-gb/"]')
    BOOKS_REF_LOCATORS = (By.CSS_SELECTOR, 'a[href="/en-gb/catalogue/category/books_2/"]')
