from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from locators import Locators
from curl import *


class TestEntryWithButtonloginToAccount:
    def test_success_entry(self, driver):
        driver.find_element(*Locators.ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTER_WAIT))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.current_url == main_site + '/'

class TestEntryWithButtonPersonalAccount:
    def test_success_entry(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCAUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE))
        assert driver.current_url == profile_endpoint
