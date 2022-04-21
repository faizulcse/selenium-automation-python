import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.chrome import ChromeDriverManager


class DriverSetup(object):
    driver = None

    def open_browser(self):
        remote_url = "http://localhost:4444/wd/hub"
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) \
            if bool(os.getenv("remote")) is False else webdriver.Remote(RemoteConnection(remote_url), options=options)
        return self.driver

    def close_browser(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver
