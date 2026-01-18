import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class LoginPage:
    """Это класс для страницы авторизации. Он содержит методы
         для ввода логина и пароля, а также для нажатия кнопки входа"""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    @allure.step("Ввод логина")
    def user_name(self, text : str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(
            {text})

    @allure.step("Ввод пароля")
    def pass_word(self, text : str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(
            {text})

    @allure.step("Нажатие кнопки входа")
    def log_in(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
