import pytest
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import host_web


url = host_web

@pytest.fixture
def browser():
    browser = webdriver.Chrome(executable_path=".chromedriver.exe")
    # browser = webdriver.Chrome()
    browser.set_window_size(1416, 1026)
    # browser.maximize_window()
    url = host_web
    # print(browser.get_window_size())
    browser.get(url=url)
    browser.set_page_load_timeout(10) # sets timeout to 10 sec
    yield browser
    browser.quit()
def test_01_templates_logs_items(browser):
    browser.find_element(By.LINK_TEXT, 'Шаблоны').click()
    assert browser.find_element(By.CLASS_NAME, 'active'), 'Шапка'
    assert browser.find_element(By.CLASS_NAME, 'button'), 'button'
    assert browser.find_element(By.CLASS_NAME, 'table-filter'), 'Фильтр'
    # assert browser.find_element(By.LINK_TEXT, 'Код'), 'Код'
    # assert browser.find_element(By.LINK_TEXT, 'ID'), 'ID'
    # assert browser.find_element(By.LINK_TEXT, 'Наименование'), 'Наименование'
    # assert browser.find_element(By.LINK_TEXT, 'Версия'), 'Наименование'
    # assert browser.find_element(By.LINK_TEXT, 'Тип события'), 'Наименование'
    # assert browser.find_element(By.LINK_TEXT, 'ID канала'), 'Наименование'
    # assert browser.find_element(By.LINK_TEXT, 'Заголовок'), 'Наименование'
    # assert browser.find_element(By.LINK_TEXT, 'Контент'), 'Наименование'
    # assert browser.find_element(By.LINK_TEXT, 'Файл'), 'Наименование'
    # assert browser.find_element(By.LINK_TEXT, 'Дата зоздания'), 'Наименование'

