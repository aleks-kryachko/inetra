import requests
from conftest import url_json1
import json
import jsonschema
from jsonschema import Draft7Validator
from jsonschema import validate
r = requests.get(url=url_json1)
def test_01_status_cod():
    assert (r.status_code == 200),'status is not 200'
def test_02_check_json():
    answer = r.json()
    answer_json = answer[0]
    assert answer_json == {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, 'wrong json'
def test_check_form_json():
    json_data = r.json()
    schema = {
        "items": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "completed": {"type": "false" or "true"}
        }}
    required: ["userId", "id", "title", "completed"]
    assert Draft7Validator(schema).is_valid(json_data), "Validation Error"
