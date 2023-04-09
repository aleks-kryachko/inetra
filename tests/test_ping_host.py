# -*- coding: utf-8 -*-
"""
http://195.189.239.54
ping страницы
:author: Aleksandr Kryachko
:copyright: Copyright 2023, Inetra Selenium Tests"
:license: MIT
:version: 1.0.0
:maintainer: Aleksandr Kryachko
:email: aleksan.kryachko@gmail.com
"""
from ping3 import ping
import requests
import pytest
import time
from conftest import host_web

def test_01_status_cod():
    r = requests.get(url=host_web)
    # print(url, r.status_code)
    assert r.status_code == 200, 'Код отклика не 200'
def test_02_ping():
    otvet = ping(host_web)
    print(otvet)
    assert otvet != True, 'сервер Offline'

