import requests
from conftest import url_json2
import json
import jsonschema
from jsonschema import Draft7Validator
from jsonschema import validate
r = requests.get(url=url_json2+'/pet')
def test_01_status_cod():
    assert (r.status_code == 200), 'status is not 200'

def test_02_check_json():
    answer = r.json()
    answer_json = answer[0]
    assert answer_json == {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, 'wrong json'
