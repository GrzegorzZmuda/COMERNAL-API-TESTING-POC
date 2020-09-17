import requests
from auth_headers import correct_header_1,incorrect_header_1
import json
import pytest
BASE = "http://127.0.0.1:5000/"
@pytest.mark.run(order=1)
def test_response_code():
    response = requests.get(BASE +"/city", headers=correct_header_1)
    assert response.status_code==200
@pytest.mark.run(order=1)
def test_response_content():
    response = requests.get(BASE +"/city", headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'
@pytest.mark.run(order=1)
def test_response_code_no_auth():
    response = requests.get(BASE +"/city")
    assert response.status_code==401

@pytest.mark.run(order=1)
def test_response_code_unauth():
    response = requests.get(BASE +"/city", headers=incorrect_header_1)
    assert response.status_code==401
@pytest.mark.run(order=1)
def test_response_types():
    response = requests.get(BASE +"/city", headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert type(response_content) == list
    for i in range(len(response_content)):
        assert type(response_content[i]["id"]) == int
        assert type(response_content[i]["inhabitants"]) == int
        assert type(response_content[i]["cityname"]) == str



