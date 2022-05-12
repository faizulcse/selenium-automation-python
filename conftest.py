import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption("--BROWSER", action="store", default=os.getenv("BROWSER"))
    parser.addoption("--REMOTE", action="store", default=os.getenv("REMOTE"))
    parser.addoption("--HEADLESS", action="store", default=os.getenv("HEADLESS"))
    parser.addoption("--DETACH", action="store", default=os.getenv("DETACH"))


@pytest.fixture(autouse=True)
def current_driver(request):
    pytest.data = request.config
    browser = request.config.getoption("--BROWSER").lower()
    remote = request.config.getoption("--REMOTE").lower()

    driver = get_driver(browser, remote)
    driver.maximize_window()
    driver.get(os.environ.get("BASE_URL"))
    driver.implicitly_wait(os.environ.get("IMPLICIT_WAIT"))
    yield driver
    if request.config.getoption("--DETACH") == "false" and driver is not None:
        driver.quit()


def get_driver(browser, remote):
    if remote == "true":
        return remote_driver(browser)
    else:
        return local_driver(browser)


def local_driver(browser):
    match browser:
        case "chrome":
            ChromeDriverManager(log_level=0)
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=get_options(browser))
        case "firefox":
            GeckoDriverManager(log_level=0)
            return webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=get_options(browser))
        case "edge":
            EdgeChromiumDriverManager(log_level=0)
            return webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=get_options(browser))
        case _:
            print("===============> Error!!! Please provide a valid browser name: " + browser)


def remote_driver(browser):
    return webdriver.Remote(RemoteConnection(os.getenv("HUB_URL")), options=get_options(browser))


def get_options(browser):
    headless = pytest.data.getoption("--HEADLESS").lower()
    detach = pytest.data.getoption("--DETACH").lower()
    match browser:
        case "chrome":
            options = webdriver.ChromeOptions()
            if headless == "true":
                options.add_argument('--headless')
            if detach == "true":
                options.add_experimental_option("detach", True)
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            return options

        case "firefox":
            options = webdriver.FirefoxOptions()
            if headless == "true":
                options.add_argument('--headless')
            return options

        case "edge":
            options = webdriver.EdgeOptions()
            if headless == "true":
                options.add_argument('--headless')
            if detach == "true":
                options.add_experimental_option("detach", True)
            return options

        case _:
            print("===============> Error!!! Please provide a valid browser name: " + browser)
