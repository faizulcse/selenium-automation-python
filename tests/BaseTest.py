import unittest

from utils.DriverSetup import DriverSetup


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.setup = DriverSetup()
        self.driver = self.setup.open_browser()
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        self.driver.get("https://www.google.com")

    def tearDown(self):
        self.setup.close_browser()
