import requests
import json
from auth_headers import correct_header_1,incorrect_header_1

BASE = "http://127.0.0.1:5000/"

def test_response_code():
    response = requests.get(BASE +"/city/2", headers=correct_header_1)
    assert response.status_code==200


def test_response_code_unauth():
    response = requests.get(BASE +"/city/2", headers=incorrect_header_1)
    assert response.status_code==401


def test_response_code_not_found():
    response = requests.get(BASE +"/city/999999", headers=correct_header_1)
    assert response.status_code==404


def test_response_code_bad_value():
    response = requests.get(BASE +"/city/99k999", headers=correct_header_1)
    assert response.status_code==404

def test_response_types():
    response = requests.get(BASE +"/city/2", headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert type(response_content["id"]) == int
    assert type(response_content["inhabitants"]) == int
    assert type(response_content["cityname"]) == str
    assert type(response_content["sensors"]) == list

def test_response_id(id=2):
    response = requests.get(BASE +"/city/"+str(id), headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert response_content["id"] == id



