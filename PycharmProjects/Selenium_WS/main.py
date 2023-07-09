from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(
    "https://www.amazon.com/Instant-Pot-60-Max-Electric/dp/B077T9YGRM/ref=sr_1_2?keywords=instant%2Bcooking%2Bpot&qid=1672082574&sr=8-2&th=1")

symbol = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[1]')
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(symbol.text + price.text)

# driver.close()  # closes the active tab you have opened
driver.quit()  # quits the entire browser
