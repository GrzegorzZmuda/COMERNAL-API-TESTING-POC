import json
from base64 import b64encode
import requests

BASE = "http://127.0.0.1:5000/"

c=":"
username = 'jan'
password = '123'
userAndPass = b64encode(username.encode("ascii") + c.encode("ascii") + password.encode("ascii")).decode("ascii")
correct_header_1 = { 'Authorization' : 'Basic %s' %  userAndPass }

c=":"
username = 'jadddn'
password = '123'
userAndPass = b64encode(username.encode("ascii") + c.encode("ascii") + password.encode("ascii")).decode("ascii")
incorrect_header_1 = { 'Authorization' : 'Basic %s' %  userAndPass }


def test_GET_city_response_code(id=2):
    response = requests.get(BASE +"/city/"+str(id), headers=correct_header_1)
    assert response.status_code==200


def test_GET_city_response_content(id=2):
    response = requests.get(BASE +"/city/"+str(id), headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'

def test_GET_city_response_code_no_auth(id=2):
    response = requests.get(BASE +"/city/"+str(id))
    assert response.status_code==401

def test_GET_city_response_code_unauth(id=2):
    response = requests.get(BASE +"/city/"+str(id), headers=incorrect_header_1)
    assert response.status_code==401


def test_GET_city_response_code_not_found(id=9999999):
    response = requests.get(BASE +"/city/"+str(id), headers=correct_header_1)
    assert response.status_code==404


def test_GET_city_response_code_bad_value(id="999jk7"):
    response = requests.get(BASE +"/city/"+id, headers=correct_header_1)
    assert response.status_code==404

def test_GET_city_response_types(id=2):
    response = requests.get(BASE +"/city/"+str(id), headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert type(response_content["id"]) == int
    assert type(response_content["inhabitants"]) == int
    assert type(response_content["cityname"]) == str
    assert type(response_content["sensors"]) == list
    for i in range(len(response_content["sensors"])):
        assert type(response_content["sensors"][i]["id"]) == int
        assert type(response_content["sensors"][i]["height"]) == int
        assert type(response_content["sensors"][i]["latitude"]) == float
        assert type(response_content["sensors"][i]["longitude"]) == float
        assert type(response_content["sensors"][i]["city_id"]) == int


def test_GET_city_response_id(id=2):
    response = requests.get(BASE +"/city/"+str(id), headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert response_content["id"] == id
    for i in range(len(response_content["sensors"])):
        assert response_content["sensors"][i]["city_id"] == id
