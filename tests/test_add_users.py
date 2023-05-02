# -*- coding: utf-8 -*-
"""
http://195.189.239.54/recipients
вкладка получатели
Добавление пользователей в БД через WEB страницу
:author: Aleksandr Kryachko
:copyright: Copyright 2023, Inetra Selenium Tests"
:license: MIT
:version: 1.0.0
:maintainer: Aleksandr Kryachko
:email: aleksan.kryachko@gmail.com
"""
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


@pytest.mark.smoke
def test_01_recipients_list(browser):
    browser.find_element(By.XPATH, '/html/body/main/form/label[2]').click()
    browser.find_element(By.CSS_SELECTOR, 'body > main > form > button').click()

    def test_01_recipients_list(browser):
        browser.find_element(By.XPATH, '/html/body/main/form/label[2]').click()
        browser.find_element(By.CSS_SELECTOR, 'body > main > form > button').click()
        m = 2
        i = 1
        while i < m:
            browser.find_element(By.LINK_TEXT, 'Получатели').click()
    # def test_09_add_recipient():
            browser.find_element(By.CLASS_NAME, 'button').click()





    def test_02(browser):
        browser.find_element(By.ID, 'last_name').click()
        browser.find_element(By.ID, 'last_name').send_keys("name")
        # browser.find_element(By.ID, 'first_name').click();
        browser.find_element(By.ID, 'first_name').send_keys('фамилия')
    # browser.find_element(By.ID, 'middle_name').click();
        browser.find_element(By.ID, 'middle_name').send_keys('отчество')

    # def test_02():
        browser.find_element(By.CLASS_NAME, 'button.button-save').click()

    # browser.find_element(By.LINK_TEXT, 'Сохранить').click()
        browser.find_element(By.LINK_TEXT, 'Получатели').click()
        browser.find_element(By.CLASS_NAME, 'table__add-icon').click()
        browser.find_element(By.CLASS_NAME, 'form-control'=='email@mail.ru').click()
        # browser.find_element(By.CLASS_NAME, 'form-control').send_keys("Email")
        # browser.find_element(By.ID, 'is_active').click()
        browser.find_element(By.CLASS_NAME, 'button.button-save').click()
        # browser.find_element(By.LINK_TEXT, 'Получатели').click()
        # # browser.find_element(By.XPATH, '/html/body/main/table/tbody/tr[1]/td[8]/a').click()
        # # browser.find_element(By.CLASS_NAME, 'form-control').click()
        # # browser.find_element(By.LINK_TEXT, 'SMS').click()
        # browser.find_element(By.ID, 'contact_info').send_keys("71234567891011")
        # browser.find_element(By.CLASS_NAME, 'button.button-save').click()
        # browser.find_element(By.LINK_TEXT, 'Получатели').click()
    # i += 1

def test_04():
    m = 5
    i = 1
    while i < m:
        print(i)
    i += 1


