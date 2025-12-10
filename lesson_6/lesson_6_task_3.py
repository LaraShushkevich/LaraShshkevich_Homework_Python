from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 20)
wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img"))
    )

images = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#award"))
    )

image = driver.find_element(By.CSS_SELECTOR, "#award")

print(image.get_attribute("src"))
    
driver.quit()
