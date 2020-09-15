import requests
import json
from auth_headers import correct_header_1,incorrect_header_1

BASE = "http://127.0.0.1:5000/"

def test_response_code(id=2):
    response = requests.get(BASE +"/city/"+str(id)+"/sensor", headers=correct_header_1)
    assert response.status_code==200


def test_response_code_unauth(id=2):
    response = requests.get(BASE +"/city/"+str(id)+"/sensor", headers=incorrect_header_1)
    assert response.status_code==401


def test_response_code_not_found(id=999999):
    response = requests.get(BASE +"/city/"+str(id)+"/sensor", headers=correct_header_1)
    assert response.status_code==404


def test_response_code_bad_value(id="k55543e"):
    response = requests.get(BASE +"/city/"+str(id)+"/sensor", headers=correct_header_1)
    assert response.status_code==404

def test_response_types(id=2):
    response = requests.get(BASE +"/city/"+str(id)+"/sensor", headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert type(response_content) == list
    for i in range(len(response_content)):
        assert type(response_content[i]["id"]) == int
        assert type(response_content[i]["height"]) == int
        assert type(response_content[i]["latitude"]) == float
        assert type(response_content[i]["longitude"]) == float
        assert type(response_content[i]["city_id"]) == int


def test_response_id(id=2):
    response = requests.get(BASE +"/city/"+str(id)+"/sensor", headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    for i in range(len(response_content)):
        assert response_content[i]["city_id"] == id