import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import host_web
from conftest import browser

# http://195.189.239.54/external-systems
# вкладка внешние системы

def test_01_templates_logs_items(browser):
    browser.find_element(By.LINK_TEXT, 'Внешние системы').click()
    assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'
    assert browser.find_element(By.CLASS_NAME, 'button'), 'button'
    assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'
    assert browser.find_element(By.LINK_TEXT, 'Код'), 'Код'
    assert browser.find_element(By.LINK_TEXT, 'ID'), 'ID'
    assert browser.find_element(By.LINK_TEXT, 'Наименование'), 'поле Наименование'
    assert browser.find_element(By.LINK_TEXT, 'Приём заданий на рассылку'), 'поле Прием задания на рассылку'
    assert browser.find_element(By.LINK_TEXT, 'Приоритет'), 'поле Приоритет'
def test_02():
    assert browser.find_element(By.CLASS_NAME, 'button').click()
    assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'
    assert browser.find_element(By.CLASS_NAME, 'button-back'), 'вернуться'
    assert browser.find_element(By.LINK_TEXT, 'Код'), 'Код'
    assert browser.find_element(By.LINK_TEXT, 'ID'), 'ID'
    assert browser.find_element(By.CLASS_NAME, 'button button-clear'), 'Очистить'