from selenium.webdriver.common.by import By

from src.pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def print_info(self):
        self.wait_for_visibility((By.NAME, "q"))
        print(self.find_element(By.NAME, "q").tag_name)
        print(self.find_elements(By.NAME, "q").__len__())
        print(self.get_driver().title)
