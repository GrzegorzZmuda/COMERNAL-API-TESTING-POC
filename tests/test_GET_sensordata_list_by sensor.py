import datetime

import requests
import json
from auth_headers import correct_header_1, incorrect_header_1

BASE = "http://127.0.0.1:5000/"
import pytest
@pytest.mark.run(order=1)
def test_response_code(id=2):
    response = requests.get(BASE + "/city/sensor/" + str(id) + "/sensordata", headers=correct_header_1)
    assert response.status_code == 200
@pytest.mark.run(order=1)
def test_response_content(id=2):
    response = requests.get(BASE + "/city/sensor/" + str(id) + "/sensordata", headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'
@pytest.mark.run(order=1)
def test_response_code_no_auth(id=2):
    response = requests.get(BASE + "/city/sensor/" + str(id) + "/sensordata")
    assert response.status_code == 401
@pytest.mark.run(order=1)
def test_response_code_unauth(id=2):
    response = requests.get(BASE + "/city/sensor/" + str(id) + "/sensordata", headers=incorrect_header_1)
    assert response.status_code == 401

@pytest.mark.run(order=1)
def test_response_code_not_found(id=999999):
    response = requests.get(BASE + "/city/sensor/" + str(id) + "/sensordata", headers=correct_header_1)
    assert response.status_code == 404

@pytest.mark.run(order=1)
def test_response_code_bad_value(id="k55543e"):
    response = requests.get(BASE + "/city/sensor/" + str(id) + "/sensordata", headers=correct_header_1)
    assert response.status_code == 404

@pytest.mark.run(order=1)
def test_response_types(id=2):
    response = requests.get(BASE + "/city/sensor/" + str(id) + "/sensordata", headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content) == list
    for i in range(len(response_content)):
        assert type(response_content[i]["id"]) == int
        assert type(response_content[i]["temperature"]) == int
        assert type(datetime.datetime.strptime(response_content[i]["measurement_datetime"],
                                               '%a, %d %b %Y %X %z')) == datetime.datetime
        assert type(response_content[i]["sensor_id"]) == int

@pytest.mark.run(order=1)
def test_response_id(id=2):
    response = requests.get(BASE + "/city/sensor/" + str(id) + "/sensordata", headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    for i in range(len(response_content)):
        assert response_content[i]["sensor_id"] == id