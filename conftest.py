import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url_ping = 'http://195.189.239.54'
url_json1 = 'http://jsonplaceholder.typicode.com/todos'
url_selenium ='http://www.python.org'
url_json2 = 'https://petstore.swagger.io/v2/pet'
host_sent =''
host_web ="http://195.189.239.54/"

@pytest.fixture
def browser():
    browser = webdriver.Chrome(executable_path=".chromedriver.exe")
    # browser = webdriver.Chrome()
    browser.set_window_size(1416, 1026)
    # browser.maximize_window()
    url = host_web
    browser.get(url=url)
    browser.set_page_load_timeout(10)
    yield browser
    browser.quit()
