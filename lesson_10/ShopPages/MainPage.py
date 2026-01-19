import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class MainPage:
    """Это класс для главной страницы магазина. Он содержит методы
             для добавления товаров в корзину и перехода в корзину"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()
