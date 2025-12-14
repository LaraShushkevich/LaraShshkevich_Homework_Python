import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options


@pytest.fixture
def driver():
    edge_options = Options()
    service = EdgeService()
    driver = webdriver.Edge(service=service, options=edge_options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    code = zip_code.value_of_css_property("background-color")
    assert code == "rgba(248, 215, 218, 1)"

    fields = ["first-name", "last-name", "address", "city", "country",
              "e-mail", "phone", "job-position", "company"]

    for field in fields:
        field_color = driver.find_element(By.ID, field)
        color = field_color.value_of_css_property("background-color")
        assert color == "rgba(209, 231, 221, 1)"

    driver.quit()
