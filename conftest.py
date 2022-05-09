import os

import pytest

from src.utils.driver_helper import open_browser, close_browser


@pytest.fixture()
def driver_init(request):
    driver = open_browser()
    driver.get(os.environ.get("BASE_URL"))
    driver.implicitly_wait(os.environ.get("IMPLICIT_WAIT"))
    driver.maximize_window()
    request.cls.driver = driver
    yield
    close_browser(driver)
