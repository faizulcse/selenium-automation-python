import pytest

from src.pages.login_page import LoginPage
from src.tests.hooks import Hooks


class TestLogin(Hooks):
    @pytest.mark.skip(reason="Skip by Tester")
    def test_method_1(self):
        print("============testmethod_1============>")

    @pytest.mark.login
    def test_method_2(self):
        login_page = LoginPage(self.driver)
        print("Session Id: " + login_page.get_session_id())
        login_page.print_info()
