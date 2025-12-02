from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()  

driver.get("http://the-internet.herokuapp.com/login")

username = "#username"
username_input = driver.find_element(By.CSS_SELECTOR, username)
username_input.send_keys("tomsmith")

sleep(2)

password = "#password"
password_input = driver.find_element(By.CSS_SELECTOR, password)
password_input.send_keys("SuperSecretPassword!")

sleep(2)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")

message_text = success_message.text.strip()

sleep(2)

print("Текст с зеленой плашки:", message_text)

driver.quit()