from selenium import webdriver
from selenium.webdriver.common.by import By
from page_object.login_page_locators import LoginPageLocators

driver = webdriver.Chrome()
link = 'http://selenium1py.pythonanywhere.com/en-gb/'
driver.get(link)

login_page_link = link + 'accounts/login/'
driver.get(login_page_link)
#email_adres = driver.find_element(By.XPATH, "//*[@id='id_login-username']")
LoginPageLocators.EMAIL_LOCATOR.send_keys("anton@google.com")
password_send = driver.find_element(By.XPATH, "//*[@id='id_login-password']")
password_send.send_keys("12345")
login_button = driver.find_element(By.XPATH, "//*[@id='login_form']/button")
login_button.click()
