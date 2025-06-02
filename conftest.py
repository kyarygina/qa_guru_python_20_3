import pytest

#selene
from selene import browser


@pytest.fixture(scope="session")
def browser_settings():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    yield
    browser.quit()

#selenium
from selenium import webdriver


@pytest.fixture(scope="session")
def driver_settings():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
