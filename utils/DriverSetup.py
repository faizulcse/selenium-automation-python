import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.remote_connection import RemoteConnection


class DriverSetup(object):
    driver = None

    def open_browser(self):
        url = "http://localhost:4444/wd/hub"
        service = Service(r"./driver/chromedriver.exe")
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless")
        if os.getenv("remote"):
            self.driver = webdriver.Remote(RemoteConnection(url), options=opts)
        else:
            self.driver = webdriver.Chrome(service=service, options=opts)
        self.driver.maximize_window()
        self.driver.get("https://www.google.com")
        return self.driver

    def close_browser(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver
