from pages.base_page import BasePage


class LoginPage(BasePage):
    def get_session_id(self):
        return self.get_driver().session_id
