import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.chrome import ChromeDriverManager


class DriverSetup(object):
    driver = None

    def open_browser(self):
        remote_url = RemoteConnection(os.getenv('hub_url'))
        options = webdriver.ChromeOptions()
        options.add_argument("--headed")
        DriverSetup.driver = webdriver.Remote(remote_url, options=options) if os.getenv("remote_run") == "true" \
            else webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return DriverSetup.driver

    def close_browser(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver
