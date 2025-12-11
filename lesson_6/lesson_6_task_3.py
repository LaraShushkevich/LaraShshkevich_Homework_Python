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

elements = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#award"))
    )

images = driver.find_elements(By.CSS_SELECTOR, "img")
# l = len(images)
# print(l)

print(images[2].get_attribute("src"))
    
driver.quit()
