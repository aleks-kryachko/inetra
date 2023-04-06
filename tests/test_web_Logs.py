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


def test_01_status_code():
    url = host_web
    responce = requests.get(url=url)
    assert responce.status_code == 200, 'status not 200'
def test_02_main_page(browser):
    assert browser.find_element(By.CLASS_NAME, 'header__title'), 'элемент МУП'
    assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка страницы'
    assert browser.find_element(By.LINK_TEXT, 'Получатели'), 'элемент Получатели'
    assert browser.find_element(By.LINK_TEXT, 'Каналы'), 'элемент Каналы'
    assert browser.find_element(By.LINK_TEXT, 'Шаблоны'), 'элемент Шаблоны'
    assert browser.find_element(By.LINK_TEXT, 'Внешние системы'), 'элемент Внешние системы'
    assert browser.find_element(By.LINK_TEXT, 'События'), 'элемент События'

    assert browser.find_element(By.LINK_TEXT, 'Журналы'), 'элемент поле Журналы'
    assert browser.find_element(By.LINK_TEXT, 'Каналы'), 'элемент поле Каналы'
    assert browser.find_element(By.LINK_TEXT, 'Получатели'), 'элемент поле Получатели'
    assert browser.find_element(By.LINK_TEXT, 'Шаблоны'),'элемент поле Шаблоны'
    assert browser.find_element(By.LINK_TEXT, 'Внешние системы'), 'элемент поле Внешние системы'

    browser.find_element(By.LINK_TEXT, 'Журналы').click()
    # browser.find_element(By.CLASS_NAME, 'header__sub').click()
    # browser.find_element(By.CLASS_NAME, 'header__nav-list').click()
    assert browser.find_element(By.LINK_TEXT, 'Журнал событий'), 'элемент  Журнал событий'
    assert browser.find_element(By.LINK_TEXT, 'Журнал оповещений'), 'элемент  Журнал оповещений'
    browser.find_element(By.LINK_TEXT, 'Журналы').click()
    assert browser.find_element(By.LINK_TEXT, 'Дата и время'), 'Дата и время'
    assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'
    assert browser.find_element(By.LINK_TEXT, 'Журнал событий'), 'Журнал событий'
    # assert browser.find_element(By.CLASS_NAME, 'button'), 'button'
    assert browser.find_element(By.CLASS_NAME, 'table-filter'), 'элемент Фильтр'
    assert browser.find_element(By.CLASS_NAME, 'main'), 'элемент таблица'
    assert browser.find_element(By.CLASS_NAME, 'column'), 'элемент шапка таблицы'
    assert browser.find_element(By.CLASS_NAME, 'active'), 'элемент Журналы'
    assert browser.find_element(By.LINK_TEXT, 'Инициатор'), 'элемент Инициатор'
    assert browser.find_element(By.LINK_TEXT, 'Тип операции'), 'элемент поле Тип операции'
    assert browser.find_element(By.LINK_TEXT, 'Статус'), 'элемент поле статус'
    assert browser.find_element(By.LINK_TEXT, 'ID запроаса'), 'элемент ID запроаса'
    assert browser.find_element(By.LINK_TEXT, 'Оповещения'), 'элемент Оповещения'
    browser.find_element(By.LINK_TEXT, 'Журнал оповещений').click()
    assert browser.find_element(By.LINK_TEXT, 'Дата и время'), 'элемент Дата и время'
    assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'элемент Фильтр'
    assert browser.find_element(By.LINK_TEXT, 'Получатель'), 'элемент Получатель'
    assert browser.find_element(By.LINK_TEXT, 'Канал'), 'элемент Канал'
    assert browser.find_element(By.LINK_TEXT, 'ID события/задания'), 'элемент ID события/задания'
    assert browser.find_element(By.LINK_TEXT, 'Статус'), 'элемент Статус'
    assert browser.find_element(By.LINK_TEXT, 'Заголовок'), 'элемент Заголовок'
    browser.find_element(By.LINK_TEXT, 'Журнал оповещений').click()
    assert browser.find_element(By.LINK_TEXT, 'Дата и время'), 'Дата и время'
    assert browser.find_element(By.LINK_TEXT, 'Получатель'), 'Получатель'
    assert browser.find_element(By.LINK_TEXT, 'Канал'), 'Канал'
    assert browser.find_element(By.LINK_TEXT, 'ID события/задания'), 'ID события/задания'
    assert browser.find_element(By.LINK_TEXT, 'Статус'), 'Статус'
    assert browser.find_element(By.LINK_TEXT, 'Заголовок'), 'Заголовок'