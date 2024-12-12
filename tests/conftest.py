import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from curl import *

# webdriver.Chrome()
# webdriver.Firefox()


# selenium.webdriver.firefox.options import Options
# selenium.webdriver.firefox.service import Service

# from locators import Locators
# from data import Credentials


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()

#Фикстура для авторизации пользователя
# @pytest.fixture
# def login(driver):
#     driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
#     driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
#     driver.find_element(*Locators.ENTRY_BUTTON).click()

