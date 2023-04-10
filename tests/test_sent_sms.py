# -*- coding: utf-8 -*-
"""
http://195.189.239.54/api/notification/email
отправка СМС
:author: Aleksandr Kryachko
:copyright: Copyright 2023, Inetra Selenium Tests
:license: MIT
:version: 1.0.0
:maintainer: Aleksandr Kryachko
:email: aleksan.kryachko@gmail.com
"""
import requests
import json
import jsonschema
from jsonschema import Draft7Validator
from jsonschema import validate
from conftest import host_web
from conftest import host_web
import pytest

url = host_web+'/api/notification/telegram'

@pytest.mark.smoke
def test_01_status_cod():
    r = requests.get(url=host_web+url)
    assert (r.status_code == 200), 'status is not 200'
print(url)
print(requests.Response)

def test_02_check_post_json(requests):
    json = {
        'phones': [
            {
                'phone': '77777777777',
            }
        ],
        'text': 'text text',
    }


response = requests.post(url=url, json=json)
answer = response.json()
answer_json = answer[0]
print(answer)
assert answer['id'] == 56, 'wrong id'
assert answer_json == {'userId': 1, 'id': 1, 'title': 'delectus aut autem',
                       'completed': False}, 'нет информации для вывода'
json_data = response.json()
schema = {
    "items": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "completed": {"type": "false" or "true"}
    }}
required: ["userId", "id", "title", "completed"]
assert Draft7Validator(schema).is_valid(json_data), "Ошибка Валидации"
print(answer_json)
