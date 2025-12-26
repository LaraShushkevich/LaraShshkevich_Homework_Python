from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def user_name(self, text):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(
            {text})

    def pass_word(self, text):
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(
            {text})

    def log_in(self):
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
