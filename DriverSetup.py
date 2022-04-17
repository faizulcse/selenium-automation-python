from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

# options = webdriver.IeOptions()
# options = webdriver.ChromeOptions()
options = webdriver.ChromeOptions()
driver = webdriver.Remote(RemoteConnection("http://localhost:4444/wd/hub"), options=options)
driver.get("https://google.com")
print(driver.title)
driver.quit()
