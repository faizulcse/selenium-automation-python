from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def my_method(self):
        print(self.get_driver().session_id)
        print(self.get_driver().title)
