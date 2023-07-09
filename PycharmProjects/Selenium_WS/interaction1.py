from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Dolamu")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Oludare")
email = driver.find_element(By.NAME, "email")
email.send_keys("oludaredolamu@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
