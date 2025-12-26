from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def enter_delay(self, value):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def enter_digits(self, text):
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def get_result(self):
        wait = WebDriverWait(self.driver, 46)
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"))
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result
