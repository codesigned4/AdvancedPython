from selenium import webdriver
import time

driver=webdriver.Chrome()

url="http://github.com"

driver.get(url)
time.sleep(2)

driver.maximize_window()
driver.save_screenshot("github.com-hompegae.png")
print("title"+driver.title)

url="https://github.com/codesigned4"
driver.get(url)

if "codesigned4" in driver.title:
    driver.save_screenshot("Github-codesigned4-page.png")

time.sleep(2)

driver.back()
driver.forward()

time.sleep(2)

driver.close()