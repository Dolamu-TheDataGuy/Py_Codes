from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://login.aliexpress.com/")

email = driver.find_element(By.ID, "fm-login-id")
email.send_keys("oludaredolamu@gmail.com")
password = driver.find_element(By.ID, "fm-login-password")
password.send_keys("Pokahunter@9")

sign_in_layer = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/button[2]")
sign_in_layer.click()



