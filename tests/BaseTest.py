import unittest

from utils.DriverSetup import DriverSetup


class BaseTest(unittest.TestCase):

    def setUp(self):
        print("=======setUp=======>")
        self.setup = DriverSetup()
        self.driver = self.setup.open_browser()

    def tearDown(self):
        self.setup.close_browser()
        print("=======tearDown=======>")
