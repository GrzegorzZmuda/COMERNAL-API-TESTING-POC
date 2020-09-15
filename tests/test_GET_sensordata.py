import requests
import json
import datetime


from auth_headers import correct_header_1,incorrect_header_1

BASE = "http://127.0.0.1:5000/"

def test_response_code(id=2):
    response = requests.get(BASE +"/sensordata/"+str(id), headers=correct_header_1)
    assert response.status_code==200


def test_response_code_unauth(id=2):
    response = requests.get(BASE +"/sensordata/"+str(id), headers=incorrect_header_1)
    assert response.status_code==401


def test_response_code_not_found(id=999999):
    response = requests.get(BASE +"/sensordata/"+str(id), headers=correct_header_1)
    assert response.status_code==404


def test_response_code_bad_value(id="k55543e"):
    response = requests.get(BASE +"/sensordata/"+id, headers=correct_header_1)
    assert response.status_code==404

def test_response_types(id=2):
    response = requests.get(BASE +"/sensordata/"+str(id), headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert type(response_content["id"]) == int
    assert type(response_content["temperature"]) == int
    assert type(datetime.datetime.strptime(response_content["measurement_datetime"],'%a, %d %b %Y %X %z')) == datetime.datetime
    assert type(response_content["sensor_id"]) == int


def test_response_id(id=2):
    response = requests.get(BASE +"/sensordata/"+str(id), headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert response_content["id"] == id

