from locators import Locators


class TestNavigationBetweenSections:
    def test_success_navigation_to_chapter_bun(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        driver.find_element(*Locators.BUN).click()
        assert driver.find_element(*Locators.CHAPTER_BUN).text == 'Булки'

    def test_success_navigation_to_chapter_sauses(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        assert driver.find_element(*Locators.CHAPTER_SAUCES).text == 'Соусы'

    def test_success_navigation_to_chapter_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        assert driver.find_element(*Locators.CHAPTER_FILLINGS).text == 'Начинки'


