import requests
import json
from auth_headers import correct_header_1,incorrect_header_1

BASE = "http://127.0.0.1:5000/"

def test_response_code(id=2):
    response = requests.get(BASE +"/city/"+str(id), headers=correct_header_1)
    assert response.status_code==200


def test_response_code_unauth(id=2):
    response = requests.get(BASE +"/city/"+str(id), headers=incorrect_header_1)
    assert response.status_code==401


def test_response_code_not_found(id=9999999):
    response = requests.get(BASE +"/city/"+str(id), headers=correct_header_1)
    assert response.status_code==404


def test_response_code_bad_value(id="999jk7"):
    response = requests.get(BASE +"/city/"+id, headers=correct_header_1)
    assert response.status_code==404

def test_response_types(id=2):
    response = requests.get(BASE +"/city/"+str(id), headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert type(response_content["id"]) == int
    assert type(response_content["inhabitants"]) == int
    assert type(response_content["cityname"]) == str
    assert type(response_content["sensors"]) == list

def test_response_id(id=2):
    response = requests.get(BASE +"/city/"+str(id), headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert response_content["id"] == id



