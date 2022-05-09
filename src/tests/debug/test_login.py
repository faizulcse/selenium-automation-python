import pytest

from pages.login_page import LoginPage
from tests.debug.test_base import BaseTest


class LoginTest(BaseTest):
    @pytest.mark.skip(reason="Skip by Tester")
    def test_method_1(self):
        print("============testmethod_1============>")

    @pytest.mark.skip(reason="Skip by Tester")
    def test_method_2(self):
        login_page = LoginPage()
        print("Session Id: " + login_page.get_session_id())
