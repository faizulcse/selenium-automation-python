import os

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.utils.DriverSetup import DriverSetup


class BasePage(DriverSetup):
    def find_element(self, *locator):
        return self.get_driver().find_element(*locator)

    def find_elements(self, *locator):
        return self.get_driver().find_elements(*locator)

    def wait_for_visibility(self, *locator):
        return self.get_fluent_wait().until(EC.visibility_of_element_located(*locator))

    def wait_for_invisibility(self, *locator):
        return self.get_fluent_wait().until(EC.invisibility_of_element_located(*locator))

    def wait_for_clickable(self, *locator):
        return self.get_fluent_wait().until(EC.element_to_be_clickable(*locator))

    def wait_for_alert(self):
        return self.get_fluent_wait().until(EC.alert_is_present())

    def get_fluent_wait(self, time_out=os.getenv('explicit_wait')):
        return WebDriverWait(self.get_driver(), time_out, 1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
