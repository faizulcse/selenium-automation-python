import os

import pytest

from src.utils.driver_helper import start_driver, stop_driver


@pytest.fixture
def browser(request):
    return request.config.getoption("--BROWSER")


@pytest.fixture
def remote(request):
    return request.config.getoption("--REMOTE")


def pytest_addoption(parser):
    parser.addoption("--BROWSER", action="store", default=os.getenv("BROWSER"))
    parser.addoption("--REMOTE", action="store", default=os.getenv("REMOTE"))


@pytest.fixture(autouse=True)
def driver_init(browser, remote):
    driver = start_driver(browser, remote)
    driver.maximize_window()
    driver.get(os.environ.get("BASE_URL"))
    driver.implicitly_wait(os.environ.get("IMPLICIT_WAIT"))
    # return driver
    yield
    stop_driver(driver)
