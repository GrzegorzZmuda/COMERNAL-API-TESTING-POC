import datetime

import requests
import json
from auth_headers import correct_header_1,incorrect_header_1

BASE = "http://127.0.0.1:5000/"

def test_response_code(id=2):
    response = requests.get(BASE +"/sensor/"+str(id), headers=correct_header_1)
    assert response.status_code==200

def test_response_content(id=2):
    response = requests.get(BASE +"/sensor/"+str(id), headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'

def test_response_code_no_auth(id=2):
    response = requests.get(BASE +"/sensor/"+str(id))
    assert response.status_code==401

def test_response_code_unauth(id=2):
    response = requests.get(BASE +"/sensor/"+str(id), headers=incorrect_header_1)
    assert response.status_code==401


def test_response_code_not_found(id=999999):
    response = requests.get(BASE +"/sensor/"+str(id), headers=correct_header_1)
    assert response.status_code==404


def test_response_code_bad_value(id="k55543e"):
    response = requests.get(BASE +"/sensor/"+id, headers=correct_header_1)
    assert response.status_code==404

def test_response_types(id=2):
    response = requests.get(BASE +"/sensor/"+str(id), headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert type(response_content["id"]) == int
    assert type(response_content["height"]) == int
    assert type(response_content["latitude"]) == float
    assert type(response_content["longitude"]) == float
    assert type(response_content["city_id"]) == int
    assert type(response_content["sensordata"]) == list
    for i in range(len(response_content["sensordata"])):
        assert type(response_content["sensordata"][i]["id"]) == int
        assert type(response_content["sensordata"][i]["temperature"]) == int
        assert type(datetime.datetime.strptime(response_content["sensordata"][i]["measurement_datetime"],
                                               '%a, %d %b %Y %X %z')) == datetime.datetime
        assert type(response_content["sensordata"][i]["sensor_id"]) == int

def test_response_id(id=2):
    response = requests.get(BASE +"/sensor/"+str(id), headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert response_content["id"] == id
    for i in range(len(response_content["sensordata"])):
        assert response_content["sensordata"][i]["sensor_id"] == id
