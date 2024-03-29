import pytest

from src.pages.login_page import LoginPage


class TestLogin:
    @pytest.mark.skip(reason="Skip by Tester")
    def test_method_1(self, current_driver):
        print("============testmethod_1============>")

    @pytest.mark.login
    def test_method_2(self, current_driver):
        login_page = LoginPage(current_driver)
        print("Session Id: " + login_page.get_session_id())
        login_page.print_info()

    @pytest.mark.parametrize("a", ["1", "2", "3"])
    def test_method_3(self, a, current_driver):
        login_page = LoginPage(current_driver)
        print("Session Id_" + a + ": " + login_page.get_session_id())
        login_page.print_info()
