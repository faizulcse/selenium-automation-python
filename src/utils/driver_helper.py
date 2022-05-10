import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def start_driver(name, is_remote):
    print("=========start browser===========>")
    return get_remote_driver(name) if is_remote.lower() == "true" else get_driver(name)


def stop_driver(driver):
    print("=========close browser===========>")
    driver.quit()


def get_driver(name):
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


def get_remote_driver(name):
    return webdriver.Remote(RemoteConnection(os.getenv("HUB_URL")), options=get_options(name))


def get_options(opts_type):
    match opts_type:
        case "chrome":
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            if os.getenv("HEADLESS").lower() == "true":
                options.add_argument('--headless')
            return options
        case "firefox":
            options = webdriver.FirefoxOptions()
            return options
        case "edge":
            options = webdriver.EdgeOptions()
            return options
        case _:
            print("===============> Error!!! Please provide a valid browser name: " + opts_type)
