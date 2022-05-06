import os
import unittest

from src.utils.DriverSetup import DriverSetup


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.setup = DriverSetup()
        self.driver = self.setup.open_browser()
        self.driver.maximize_window()
        self.driver.implicitly_wait(os.environ.get('implicit_wait'))
        self.driver.get(os.environ.get('base_url'))

    def tearDown(self):
        self.setup.close_browser()
