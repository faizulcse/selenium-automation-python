from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_session_id(self):
        return self.get_driver().session_id

    def print_info(self):
        self.wait_for_visibility((By.NAME, "q"))
        print(self.find_element(By.NAME, "q").tag_name)
        print(self.find_elements(By.NAME, "q").__len__())
        print(self.get_driver().title)
