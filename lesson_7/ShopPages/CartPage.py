from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def cart_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
