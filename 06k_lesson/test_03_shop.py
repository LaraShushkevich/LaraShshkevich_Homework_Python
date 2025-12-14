import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(
        "standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(
        "secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    WebDriverWait(driver, 5).until(EC.url_contains("inventory.html"))

    driver.find_element(By.CSS_SELECTOR,
                        "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    WebDriverWait(driver, 5).until(EC.url_contains("cart.html"))
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    WebDriverWait(driver, 5).until(EC.url_contains("checkout-step-one.html"))
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Лариса")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Шушкевич")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("12345")

    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    WebDriverWait(driver, 5).until(EC.url_contains("checkout-step-two.html"))
    total_element = driver.find_element(By.CSS_SELECTOR,
                                        ".summary_total_label")
    actual_total_text = total_element.text
    actual_total_value = actual_total_text.split(": ")[-1]

    expected_total = "$58.29"
    assert actual_total_value == expected_total
    driver.quit()
