from ping3 import ping
import requests
import pytest
import time
from conftest import url_ping

def test_01_status_cod():
    r = requests.get(url=url_ping)
    # print(url, r.status_code)
    assert r.status_code == 200, 'Код отклика не 200'
def test_02_ping():
    otvet = ping(url_ping)
    print(otvet)
    assert otvet == True, 'сервер Offline'

