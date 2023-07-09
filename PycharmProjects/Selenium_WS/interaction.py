from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

# header = driver.find_elements(By.ID, "mp-topbanner")

# for head in header:
# data = head.find_element(By.ID, "articlecount")
# article_count = data.text.split()[0]
# print(article_count)
