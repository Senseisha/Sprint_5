from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import generate_registration
from locators import Locators
from curl import *


class TestRegistrationWithNewCredentials:
    def test_success_registration(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.NEW_USER).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION))

        name, email, password = generate_registration()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_TEXT))
        assert driver.current_url == auth_endpoint


class TestRegistrationWithWrongPassword:
    def test_failed_registration(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.NEW_USER).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION))

        name, email, password = generate_registration()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('36987')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FAILED)).text
        assert reg_text == 'Некорректный пароль'


