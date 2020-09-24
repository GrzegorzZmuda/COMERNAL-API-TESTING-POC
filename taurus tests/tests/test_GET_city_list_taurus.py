from base64 import b64encode

import requests

import json
import pytest
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
@pytest.mark.run(order=1)
def test_GET_city_list_response_code():
    response = requests.get(BASE +"/city", headers=correct_header_1)
    assert response.status_code==200
@pytest.mark.run(order=1)
def test_GET_city_list_response_content():
    response = requests.get(BASE +"/city", headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'
@pytest.mark.run(order=1)
def test_GET_city_list_response_code_no_auth():
    response = requests.get(BASE +"/city")
    assert response.status_code==401

@pytest.mark.run(order=1)
def test_GET_city_list_response_code_unauth():
    response = requests.get(BASE +"/city", headers=incorrect_header_1)
    assert response.status_code==401
@pytest.mark.run(order=1)
def test_GET_city_list_response_types():
    response = requests.get(BASE +"/city", headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert type(response_content) == list
    for i in range(len(response_content)):
        assert type(response_content[i]["id"]) == int
        assert type(response_content[i]["inhabitants"]) == int
        assert type(response_content[i]["cityname"]) == str



