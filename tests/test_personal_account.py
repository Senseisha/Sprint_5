from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *


class TestGoToPersonalAccount:
    def test_success_transition(self, login):
        driver = login

        driver.find_element(*Locators.PERSONAL_ACCAUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE))
        assert driver.current_url == profile_endpoint


class TestGoToConstructor:
    def test_success_transition(self, login):
        driver = login

        driver.find_element(*Locators.PERSONAL_ACCAUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE))
        driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BURGER))
        assert driver.current_url == main_site + '/'


class TestGoToLogo:

    def test_success_transition(self, login):
        driver = login

        driver.find_element(*Locators.PERSONAL_ACCAUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BURGER))
        assert driver.current_url == main_site + '/'

