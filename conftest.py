import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.chrome import ChromeDriverManager


def open_browser():
    remote_url = RemoteConnection(os.getenv('HUB_URL'))
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if os.getenv("HEADLESS").lower() == "true":
        options.add_argument('--headless')

    if os.getenv("REMOTE_RUN").lower() == "true":
        driver = webdriver.Remote(remote_url, options=options)
    else:
        ChromeDriverManager(log_level=0)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.maximize_window()
    driver.implicitly_wait(os.environ.get('IMPLICIT_WAIT'))
    driver.get(os.environ.get('BASE_URL'))
    return driver


@pytest.fixture(autouse=True)
def driver_init():
    print("<===============Open Browser==============>")
    driver = open_browser()
    pytest.driver = driver
    yield
    print("<===============Close Browser==============>")
    driver.quit()
