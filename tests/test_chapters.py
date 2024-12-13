from locators import Locators


class TestChapterBun:
    def test_test_success_transition(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        driver.find_element(*Locators.BUN).click()
        assert driver.find_element(*Locators.CHAPTER_BUN).text == 'Булки'


class TestChapterSauces:
    def test_test_success_transition(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        assert driver.find_element(*Locators.CHAPTER_SAUCES).text == 'Соусы'


class TestChapterFillings:
    def test_test_success_transition(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        assert driver.find_element(*Locators.CHAPTER_FILLINGS).text == 'Начинки'


