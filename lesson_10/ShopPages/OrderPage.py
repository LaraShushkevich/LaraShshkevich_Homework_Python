import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    """Это класс для страницы оформления заказа. Он содержит методы
     для заполнения формы данными (имя, фамилия, почтовый индекс)
     и проверки итоговой стоимости"""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    @allure.step("Ввод имени покупателя")
    def first_name(self, text : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys({text})

    @allure.step("Ввод фамилии покупателя")
    def last_name(self, text : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys({text})

    @allure.step("Ввод почтового индекса покупателя")
    def postal_code(self, text : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys({text})

    @allure.step("Получение итоговой стоимости заказа")
    def check_sum(self) -> str:
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        WebDriverWait(self.driver, 5).until(
            EC.url_contains("checkout-step-two.html"))
        total_element = self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label")
        actual_total_text = total_element.text
        actual_total_value = actual_total_text.split(": ")[-1]

        return actual_total_value
