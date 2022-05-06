import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.chrome import ChromeDriverManager


def open_browser():
    remote_url = RemoteConnection(os.getenv('hub_url'))
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if os.getenv("headless").upper() == "TRUE":
        options.add_argument('--headless')
    driver = webdriver.Remote(remote_url, options=options) if os.getenv("remote_run").upper() == "TRUE" \
        else webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(os.environ.get('implicit_wait'))
    driver.get(os.environ.get('base_url'))
    pytest.driver = driver


def close_browser():
    pytest.driver.quit()


@pytest.fixture()
def browser_setup():
    open_browser()
    yield
    close_browser()
