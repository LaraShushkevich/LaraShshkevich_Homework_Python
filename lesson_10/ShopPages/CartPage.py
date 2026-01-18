import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class CartPage:
    """Это класс для страницы корзины. Он содержит методы
                 для нажатия кнопки Checkout и проверки содержимого корзины"""
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    @allure.step("Нажатие кнопки Checkout")
    def cart_checkout(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
