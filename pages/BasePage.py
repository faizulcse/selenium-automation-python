from utils.DriverSetup import DriverSetup


class BasePage(DriverSetup):
    def find_element(self, *locator):
        return self.get_driver().find_element(*locator)

    def find_elements(self, *locator):
        return self.get_driver().find_elements(*locator)

    def wait_for_visibility(self, *locator):
        return self.get_driver().find_element(*locator)

    def wait_for_invisibility(self, *locator):
        return self.get_driver().find_element(*locator)
