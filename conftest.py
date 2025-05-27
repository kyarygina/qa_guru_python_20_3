import pytest

#selenide
from selene import browser


@pytest.fixture(scope="session")
def browser_settings():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    yield
    browser.quit()

#selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(service=Service())
    driver.set_window_size(1920, 1080)
    yield
    driver.quit()