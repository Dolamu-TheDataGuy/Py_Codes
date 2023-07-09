from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=PATH)

driver.get("https://www.techwithtim.net/")

link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Get Started"))
    )
    element.click()

    driver.back()  # to go a page backward
    driver.back()
    driver.back()
    driver.forward()  # to go a page forward
except:
    driver.quit()
