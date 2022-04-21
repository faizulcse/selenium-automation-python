import os
import unittest

from utils.DriverSetup import DriverSetup


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.setup = DriverSetup()
        self.driver = self.setup.open_browser()
        self.driver.maximize_window()
        self.driver.implicitly_wait(os.environ.get('IMPLICIT_WAIT'))
        self.driver.get(os.environ.get('BASE_URL'))

    def tearDown(self):
        self.setup.close_browser()
