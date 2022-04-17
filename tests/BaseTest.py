import unittest

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://localhost:4444/wd/hub"
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(RemoteConnection(self.url), options=options)

        # self.driver = webdriver.Chrome(
        #     executable_path=r"C:\Users\BS705\PycharmProjects\selenium-automation-python\driver\chromedriver.exe")

        self.driver.maximize_window()
        self.driver.get("https://www.google.com")

    def tearDown(self):
        self.driver.quit()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
