import pytest

from src.pages.login_page import LoginPage


class TestLogin:
    @pytest.mark.skip(reason="Skip by Tester")
    def test_method_1(self, driver):
        print("============testmethod_1============>")

    @pytest.mark.login
    def test_method_2(self, driver):
        login_page = LoginPage(driver)
        print("Session Id: " + login_page.get_session_id())
        login_page.print_info()
