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
import pytest
import requests
import json
import jsonschema
from jsonschema import Draft7Validator
from jsonschema import validate
from conftest import host_web

url = "http://195.189.239.54/api/notification" \
      "{event_id: 4}"

@pytest.mark.smoke
def test_01_status_cod():
    # url = host_web+'/api/notification/'
    r = requests.get(url=url)
    assert (r.status_code == 200), 'status is not 200'
    print(requests.Response)

def test_02_check_send_event():
    json = {"event_id": 11}
    url = "http://195.189.239.54/api/notification"
    response = requests.post(url=url, json=json) # http://195.189.239.53/api/notification/?event_id=11
    answer = response.json()
    answer_json = answer[0]
    print(answer)
    # assert answer == 'Message send successfully!', 'wrong answer'
    # assert (response.status_code == 200), 'status is not 200'
# json_data = response.json()
# schema = {
#     {
#     'emails': [
#         {
#             'email': 'aleksan.kryachko@gmail.com',
#             'subject': 'mail subject',
#             'text': 'custom text',
#         }
#     ]
# }}
#
# required: ["userId", "id", "title", "completed"]
# assert Draft7Validator(schema).is_valid(json_data), "Ошибка Валидации"
# print(answer_json)
