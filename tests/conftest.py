# webdriver.Chrome()
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from locators import Locators
from data import Credentials


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()


# Фикстура для авторизации пользователя
@pytest.fixture
def login(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_TEXT))
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.ENTRY_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    return driver
