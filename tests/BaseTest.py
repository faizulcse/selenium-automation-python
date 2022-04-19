import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.remote_connection import RemoteConnection


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://localhost:4444/wd/hub"
        self.opts = webdriver.ChromeOptions()
        self.service = Service(r"C:\Users\BS705\PycharmProjects\selenium-automation-python\driver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service, options=self.opts) if (
                os.getenv("remote") is None) else webdriver.Remote(RemoteConnection(self.url), options=self.opts)
        self.driver.maximize_window()
        self.driver.get("https://www.google.com")

    def tearDown(self):
        self.driver.quit()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
