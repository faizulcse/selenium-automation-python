import os

import pytest

from src.utils.driver_helper import get_driver


def pytest_addoption(parser):
    parser.addoption("--BROWSER", action="store", default=os.getenv("BROWSER"))
    parser.addoption("--REMOTE", action="store", default=os.getenv("REMOTE"))
    parser.addoption("--HEADLESS", action="store", default=os.getenv("HEADLESS"))
    parser.addoption("--DETACH", action="store", default=os.getenv("DETACH"))


@pytest.fixture(autouse=True)
def driver(request):
    pytest.data = request.config
    web_driver = get_driver()
    yield web_driver
    if pytest.data.getoption("--DETACH") == "false" and driver is not None:
        web_driver.quit()
