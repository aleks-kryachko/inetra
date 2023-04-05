import pytest
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import host_web
from conftest import browser


url = host_web

# @pytest.fixture
# def browser():
#     browser = webdriver.Chrome(executable_path=".chromedriver.exe")
#     # browser = webdriver.Chrome()
#     browser.set_window_size(1416, 1026)
#     # browser.maximize_window()
#     url = host_web
#     # print(browser.get_window_size())
#     browser.get(url=url)
#     browser.set_page_load_timeout(10) # sets timeout to 10 sec
#     yield browser
#     browser.quit()


def test_01_status_code():
    url = host_web
    responce = requests.get(url=url)
    assert responce.status_code == 200, 'status not 200'
def test_02_main_page(browser):
    assert browser.find_element(By.CLASS_NAME, 'header__title'), 'Логотипа нет'
    assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Главная страница отсутствует'
    assert browser.find_element(By.LINK_TEXT, 'Получатели')
def test_03_main_page_elements(browser):
    assert browser.find_element(By.LINK_TEXT, 'Журналы'), 'Журналы'
    assert browser.find_element(By.LINK_TEXT, 'Каналы'), 'Каналы'
    assert browser.find_element(By.LINK_TEXT, 'Получатели'), 'Получатели'
    assert browser.find_element(By.LINK_TEXT, 'Шаблоны'),'Шаблоны'
    assert browser.find_element(By.LINK_TEXT, 'Внешние системы'), 'Внешние системы'
def test_04_header__nav_list_elements(browser):
    browser.find_element(By.LINK_TEXT, 'Журналы').click()
    # browser.find_element(By.CLASS_NAME, 'header__sub').click()
    # browser.find_element(By.CLASS_NAME, 'header__nav-list').click()
    assert browser.find_element(By.LINK_TEXT, 'Журнал событий'), 'Журнал событий'
    assert browser.find_element(By.LINK_TEXT, 'Журнал событий'), 'Журнал событий'
def test_05_Event_log_elements(browser):
    # assert browser.find_element(By.LINK_TEXT, 'Журналы').click()
    assert browser.find_element(By.CLASS_NAME, 'button'), 'button'
    assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'
    assert browser.find_element(By.CLASS_NAME, 'main'), 'таблица'
    assert browser.find_element(By.CLASS_NAME, 'column'), 'шапка таблицы'
    assert browser.find_element(By.CLASS_NAME, 'active'), ':Журналы'
    # browser.find_element(By.CLASS_NAME, 'active').click()
    assert browser.find_element(By.LINK_TEXT, 'Дата и время'), 'Дата и время'
    assert browser.find_element(By.LINK_TEXT, 'Инициатор'), 'Инициатор'
    assert browser.find_element(By.LINK_TEXT, 'Тип операции'), 'Тип операции'
    assert browser.find_element(By.LINK_TEXT, 'ID запроаса'), 'ID запроаса'
    assert browser.find_element(By.LINK_TEXT, 'Оповещение'), 'Оповещение'

def test_06_Notification_log_elements(browser):
    browser.find_element(By.LINK_TEXT, 'Журнал оповещений').click()
    assert browser.find_element(By.LINK_TEXT, 'Дата и время'), 'Дата и время'
    assert browser.find_element(By.LINK_TEXT, 'Получатель'), 'Получатель'
    assert browser.find_element(By.LINK_TEXT, 'Канал'), 'Канал'
    assert browser.find_element(By.LINK_TEXT, 'ID события/задания'), 'ID события/задания'
    assert browser.find_element(By.LINK_TEXT, 'Статус'), 'Статус'
    assert browser.find_element(By.LINK_TEXT, 'Заголовок'), 'Заголовок'