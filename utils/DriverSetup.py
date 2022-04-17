# import unittest
#
# from selenium import webdriver
#
#
# class DriverSetup(unittest.TestCase):
#     driver = None
#
#     @classmethod
#     def open_browser(cls):
#         print("Test Started================>")
#         driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
#         driver.maximize_window()
#         driver.get("https://www.google.com")
#         print("Test Started")
#
#     @classmethod
#     def close_browser(cls):
#         cls.driver.quit()
#         print("Test Complete")
