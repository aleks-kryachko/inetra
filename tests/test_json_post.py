# https://www.postman.com/mitshex1/workspace/swagger-petstore/documentation/16308298-86c562b6-bafe-415a-b874-9ccc6590842f


import requests
from conftest import url_json2
import json
import jsonschema
from jsonschema import Draft7Validator
from jsonschema import validate

def test_01_status_cod():
    r = requests.get(url=url_json2)
    assert (r.status_code == 200), 'status is not 200'

# Add a new pet to the store
def test_02_check_post_json():
    json = {
    "name": "doggie",

    "id": -36071088,
    "category": {
        "id": 36135777,
        "name": "laborum elit"
    },
    "tags": [
        {
            "id": -58986065,
            "name": "id ut dolore ipsum dol"
        },
        {
            "id": -20316514,
            "name": "adipisicing nostrud"
        }
    ],
    "status": "available"
}

    response = requests.post((url_json2),  json=json)
    answer = response.json()
    # answer_json = answer[0]
    print(answer) #{'id': 9223372036854766053, 'category': {'id': 36135777, 'name': 'laborum elit'}, 'name': 'doggie', 'photoUrls': ['elit cillum exercitation', 'tempor cupidatat sint aliqua'], 'tags': [{'id': -58986065, 'name': 'id ut dolore ipsum dol'}, {'id': -20316514, 'name': 'adipisicing nostrud'}], 'status': 'available'}

    d = answer['id']

    assert answer['id'] == d, 'wrong id'
    # assert answer['petId'] == 17588388, 'wrong petId'
    # assert answer['status'] == 'approved', 'wrong status'
    return d
# Find pet by ID
def test_03_check_create_pet(d):
    d = test_03_check_create_pet(d)
    # print(d)
    response = requests.get(f'https://petstore.swagger.io/v2/pet/{d}')
    answer = response.json()
    print(answer) #{'id': 9223372036854766283, 'category': {'id': 36135777, 'name': 'laborum elit'}, 'name': 'doggie', 'photoUrls': ['elit cillum exercitation', 'tempor cupidatat sint aliqua'], 'tags': [{'id': -58986065, 'name': 'id ut dolore ipsum dol'}, {'id': -20316514, 'name': 'adipisicing nostrud'}], 'status': 'available'}
    # 9223372036854766591 9223372036854766283 9223372036854766782 9223372036854766860 9223372036854766933
    assert answer['id'] == d, 'wrong id'
    assert answer['name'] == 'laborum elit', 'wrong name'