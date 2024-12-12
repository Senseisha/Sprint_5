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

#Фикстура для входа в аккаунт
# @pytest.fixture
# def registrarion():
#     options = Options()
#     options.add_argument("--window-size=1200,600")
#     browser = webdriver.Chrome(options=options)
#     browser.get(register_endpoint)
#
#     # driver.find_element(*Locators.ACCAUNT_BUTTON).click()
#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.NAME))
#     # driver.find_element(*Locators.NEW_USER).click()
#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTERATION))
#     yield browser
#     browser.quit()