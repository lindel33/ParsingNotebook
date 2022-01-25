import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, SessionNotCreatedException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())


def get_browser(site_url: str):
    """
    Получение браузера в объект browser
    :return: browser
    """
    try:
        browser = webdriver.Chrome(service=s)
        browser.maximize_window()
        browser.get(site_url)
        time.sleep(2)
        return browser

    except SessionNotCreatedException:
        print('TimeoutException')
