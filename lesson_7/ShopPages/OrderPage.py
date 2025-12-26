from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def first_name(self, text):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys({text})

    def last_name(self, text):
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys({text})

    def postal_code(self, text):
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys({text})

    def check_sum(self):
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        WebDriverWait(self.driver, 5).until(
            EC.url_contains("checkout-step-two.html"))
        total_element = self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label")
        actual_total_text = total_element.text
        actual_total_value = actual_total_text.split(": ")[-1]

        return actual_total_value
