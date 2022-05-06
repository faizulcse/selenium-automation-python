import unittest

import pytest


@pytest.mark.usefixtures("browser_setup")
class BaseTest(unittest.TestCase):
    @pytest.mark.skip
    def test_method_1(self):
        print("============testmethod_1============>")

    @pytest.mark.skip
    def test_method_2(self):
        print(pytest.driver.title)
        print("============testmethod_2============>")

    def test_method(self):
        print("=================>")
