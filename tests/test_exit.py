from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *

class TestExit:
    def test_success_exit(self, login):
        driver = login

        driver.find_element(*Locators.PERSONAL_ACCAUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE))
        driver.find_element(*Locators.EXIT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_TEXT))
        assert driver.current_url == auth_endpoint

