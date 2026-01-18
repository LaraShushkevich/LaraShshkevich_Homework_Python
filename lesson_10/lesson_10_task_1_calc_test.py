import  allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage

@allure.title("Тестирование калькулятора: 7+8=15")
@allure.suite("Домашнее задание по Allure")
@allure.description("Проверка корректности работы калькулятора")
@allure.feature("SLOW CALC")
@allure.severity("normal")
def test_slow_calc():
    """Тест на проверку функциональности калькулятора: Открыть страницу калькулятора.
       Ввести значение 45  в поле задержки (локатор #delay).
       Нажать кнопки: 7, +, 8, =.
       Проверить, что в окне отобразится результат 15  через 45 секунд."""


    driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    calc_page = CalculatorPage(driver)

    calc_page.enter_delay("45")

    calc_page.enter_digits("7")
    calc_page.enter_digits("+")
    calc_page.enter_digits("8")
    calc_page.enter_digits("=")

    result = calc_page.get_result()

    with allure.step("Проверка, что результат равен 15"):
        assert result == "15"

    driver.quit()
