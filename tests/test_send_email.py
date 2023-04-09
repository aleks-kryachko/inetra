# -*- coding: utf-8 -*-
"""
http://195.189.239.54/api/notification/sms
отправка EMail
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

url = host_web+'/api/notification/sms'


def test_01_status_cod():
    # url = host_web+'/api/notification/sms'
    r = requests.get(url=url)
    assert (r.status_code == 200), 'status is not 200'
    print(requests.Response)

def test_02_check_post_json(requests):
    json = {
    'tokens': [
        {
            'token': 'tr6y5rn7658mi7rouyg9f6dt76j6u',
        }
    ],
    'title': 'push title',
    'text': 'push text',
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
