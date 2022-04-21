from utils.DriverSetup import DriverSetup


class BasePage(DriverSetup):
    def wait_for_visibility(self):
        pass

    def wait_for_invisibility(self):
        pass
