import requests
from auth_headers import correct_header_1,incorrect_header_1
import json

BASE = "http://127.0.0.1:5000/"

def test_response_code():
    response = requests.get(BASE +"/sensor", headers=correct_header_1)
    assert response.status_code==200


def test_response_code_unauth():
    response = requests.get(BASE +"/sensor", headers=incorrect_header_1)
    assert response.status_code==401

def test_response_types():
    response = requests.get(BASE +"/sensor", headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert type(response_content) == list
    for i in range(len(response_content)):
        assert type(response_content[i]["id"]) == int
        assert type(response_content[i]["height"]) == int
        assert type(response_content[i]["latitude"]) == float
        assert type(response_content[i]["longitude"]) == float
        assert type(response_content[i]["city_id"]) == int