import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver():
    browser = pytest.data.getoption("--BROWSER").lower()
    remote = pytest.data.getoption("--REMOTE").lower()
    driver = remote_driver(browser) if remote == "true" else local_driver(browser)
    driver.maximize_window()
    driver.get(os.environ.get("BASE_URL"))
    driver.implicitly_wait(os.environ.get("IMPLICIT_WAIT"))
    return driver


def local_driver(name):
    match name:
        case "chrome":
            ChromeDriverManager(log_level=0)
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=get_options(name))
        case "firefox":
            GeckoDriverManager(log_level=0)
            return webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=get_options(name))
        case "edge":
            EdgeChromiumDriverManager(log_level=0)
            return webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=get_options(name))
        case _:
            print("===============> Error!!! Please provide a valid browser name: " + name)


def remote_driver(name):
    return webdriver.Remote(RemoteConnection(os.getenv("HUB_URL")), options=get_options(name))


def get_options(opts_name):
    headless = pytest.data.getoption("--HEADLESS").lower()
    detach = pytest.data.getoption("--DETACH").lower()
    match opts_name:
        case "chrome":
            options = webdriver.ChromeOptions()
            if headless == "true":
                options.add_argument('--headless')
            if detach == "true":
                options.add_experimental_option("detach", True)
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
            print("===============> Error!!! Please provide a valid browser name: " + opts_name)
