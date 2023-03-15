import pytest
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import url_selenium
@pytest.fixture
def browser():
    browser = webdriver.Chrome(executable_path=".chromedriver.exe")
    browser = webdriver.Chrome()
    browser.set_window_size(1416, 1026)
    # browser.maximize_window()
#     url = 'http://www.python.org'
    print(browser.get_window_size())
    browser.get(url=url_selenium)
    browser.set_page_load_timeout(10) # sets timeout to 10 sec
    yield browser
    browser.quit()


def test_01_status_code():
    url = 'http://www.python.org'
    r = requests.get(url=url_selenium)
    assert r.status_code == 200, 'status not 200'

def test_02_main_page(browser):
    assert browser.find_element(By.CSS_SELECTOR, '#downloads > a'), 'Download'
    assert browser.find_element(By.CSS_SELECTOR, "#documentation > a"), 'Button community'
    assert browser.find_element(By.NAME, 'q'), 'Search'
    assert browser.find_element(By.ID, 'submit'), 'button Go'
    assert browser.find_element(By.CLASS_NAME, 'container'), 'container test python'
    assert browser.find_element(By.CLASS_NAME, 'site-headline'), 'logo python tm'