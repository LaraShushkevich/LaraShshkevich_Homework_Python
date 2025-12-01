from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.google.com")
driver.get("http://uitestingplayground.com/dynamicid")

dynamic_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
dynamic_button.click()
print("Кнопка нажата успешно!")

sleep(5)