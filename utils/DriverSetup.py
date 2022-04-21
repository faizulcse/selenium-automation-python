import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.chrome import ChromeDriverManager


class DriverSetup(object):
    driver = None

    def open_browser(self):
        remote_url = RemoteConnection(os.getenv('HUB_URL'))
        service = Service(ChromeDriverManager().install())
        remote_run = os.getenv("REMOTE_RUN")
        options = webdriver.ChromeOptions()
        options.add_argument("--headed")
        self.driver = webdriver.Remote(remote_url, options=options) \
            if remote_run == "True" else webdriver.Chrome(service=service, options=options)
        return self.driver

    def close_browser(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver
