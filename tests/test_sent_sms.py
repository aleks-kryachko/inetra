import requests
from conftest import host_sent
import json
import jsonschema
from jsonschema import Draft7Validator
from jsonschema import validate

url = f'host_sent+"/api/notification/email"'


def test_01_status_cod():
    r = requests.get(url=url)
    assert (r.status_code == 200), 'status is not 200'


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
