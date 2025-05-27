from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_successful_search(driver_settings):
    driver = driver_settings
    driver.get('https://www.startpage.com/')

    search_input = driver.find_element(By.ID, 'q')
    search_input.send_keys('qa.guru')
    search_input.send_keys(Keys.RETURN)

    time.sleep(2)

    assert 'Web results' in driver.page_source
    driver.quit()

def test_unsuccessful_search(driver_settings):
        driver = driver_settings
        driver.get('https://www.startpage.com/')

        search_input = driver.find_element(By.ID, 'q')
        search_input.send_keys('ergaegrakjnjhwebfjaw3yhya7rgfawbhe`a')
        search_input.send_keys(Keys.RETURN)

        time.sleep(2)

        assert 'Uh-oh, there are no results for this search.' in driver.page_source
        driver.quit()