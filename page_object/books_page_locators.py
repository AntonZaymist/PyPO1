from selenium.webdriver.common.by import By


class BooksPageLocators:
    HEADER_LOCATORS = (By.CSS_SELECTOR, "div.page-header.action > h1")
    SITE_TREE_LOCATORS = (By.CSS_SELECTOR, "ul.breadcrumb > li.active")
    INPUT_SEARCH_LOCATORS = (By.XPATH, "//*[@id='id_q']")
    BUTTON_SEARCH_LOCATORS = (By.XPATH, "//input[@type='submit']")
