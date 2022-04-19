import pytest

from tests.BaseTest import BaseTest


class LoginTest(BaseTest):
    @pytest.mark.login
    def test_first(self):
        print("\n" + self.driver.title)

    @pytest.mark.login
    def test_second(self):
        print("\n" + self.driver.title)

    @pytest.mark.login
    def test_third(self):
        print("\n" + self.driver.title)