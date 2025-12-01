from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()  

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    wait = WebDriverWait(driver, 10)
    input_field = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "input"))
    )

    driver.execute_script(
        "arguments[0].setAttribute('type', 'text');", 
        input_field
    )
    
    input_field.send_keys("Sky")
    
    sleep(3)

    input_field.clear()

    sleep(3)
    
    input_field.send_keys("Pro")
    
finally:
    driver.quit()