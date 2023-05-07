import os.path
import time

from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from property import RESOURCES_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp

def test_file_downloading_browser():
    tmp = os.path.join(RESOURCES_PATH, 'pytest-main.zip.crdownload')
    options = webdriver.ChromeOptions()
    if not os.path.exists(RESOURCES_PATH):
        os.mkdir(RESOURCES_PATH)
    prefs = {
        "download.default_directory": RESOURCES_PATH,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()

    file_size = os.path.getsize(tmp)
    assert file_size == 62744
    os.remove(tmp)