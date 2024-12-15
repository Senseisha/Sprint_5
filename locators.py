from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    NAME = (By.CSS_SELECTOR, ".input__textfield[name='name']")
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")
    PASSWORD = (By.CSS_SELECTOR, ".input__textfield[type='password']")
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    REGISTRATION = (By.XPATH, ".//h2[text()='Регистрация']")
    NEW_USER = (By.LINK_TEXT, "Зарегистрироваться")
    FAILED = (By.XPATH, ".//p[text()='Некорректный пароль']")

    # Локаторы для входа
    ORDER_TEXT = (By.XPATH, ".//h2[text()='Вход']")
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    ENTRY_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    REGISTERED_USER = (By.LINK_TEXT, "Войти")

    #Локаторы для восстановления пароля
    PASSWORD_RECOVERY = (By.LINK_TEXT, "Восстановить пароль")
    PASSWORD_RECOVERY_TEXT = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    RESTORE = (By.XPATH, ".//button[text()='Восстановить']")
    NEW_PASSWORD = (By.NAME, "Введите новый пароль")
    REMEMBERED_PASSWORD =(By.LINK_TEXT, "Войти")

    # Локаторы для входа и выхода из Личного кабинета
    PERSONAL_ACCAUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")
    PROFILE = (By.XPATH, ".//a[text()='Профиль']")
    EXIT = (By.XPATH, ".//button[text()='Выход']")

    #Локаторы для перехода из личного кабинета
    CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
    LOGO = (By.XPATH, ".//a[@href='/']")
    BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")

    #Локаторы для перехода по категориям
    BUN = (By.XPATH, ".//span[text()='Булки']")
    CHAPTER_BUN = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__')]")

    SAUCES = (By.XPATH, ".//span[text()='Соусы']")
    CHAPTER_SAUCES = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__')]")

    FILLINGS = (By.XPATH, ".//span[text()='Начинки']")
    CHAPTER_FILLINGS = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__')]")


