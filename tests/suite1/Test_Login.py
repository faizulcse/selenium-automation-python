import pytest

from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class LoginTest(BaseTest):
    @pytest.mark.login
    def test_first(self):
        login = LoginPage(self.driver)
        login.print_info()

    @pytest.mark.login
    def test_second(self):
        login = LoginPage(self.driver)
        login.print_info()

    @pytest.mark.login
    def test_third(self):
        login = LoginPage(self.driver)
        login.print_info()
