from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage


def test_slow_calc():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    calc_page = CalculatorPage(driver)
    calc_page.enter_delay("45")
    calc_page.enter_digits("7")
    calc_page.enter_digits("+")
    calc_page.enter_digits("8")
    calc_page.enter_digits("=")
    result = calc_page.get_result()

    assert result == "15"

    driver.quit()
