import requests
import json
import datetime
import pytest
from base64 import b64encode

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
def test_GET_sensordata_response_code(id=2):
    response = requests.get(BASE +"/sensordata/"+str(id), headers=correct_header_1)
    assert response.status_code==200
@pytest.mark.run(order=1)
def test_GET_sensordata_response_content(id=2):
    response = requests.get(BASE +"/sensordata/"+str(id), headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'
@pytest.mark.run(order=1)
def test_GET_sensordata_response_code_no_auth(id=2):
    response = requests.get(BASE +"/sensordata/"+str(id))
    assert response.status_code==401
@pytest.mark.run(order=1)
def test_GET_sensordata_response_code_unauth(id=2):
    response = requests.get(BASE +"/sensordata/"+str(id), headers=incorrect_header_1)
    assert response.status_code==401

@pytest.mark.run(order=1)
def test_GET_sensordata_response_code_not_found(id=999999):
    response = requests.get(BASE +"/sensordata/"+str(id), headers=correct_header_1)
    assert response.status_code==404

@pytest.mark.run(order=1)
def test_GET_sensordata_response_code_bad_value(id="k55543e"):
    response = requests.get(BASE +"/sensordata/"+id, headers=correct_header_1)
    assert response.status_code==404
@pytest.mark.run(order=1)
def test_GET_sensordata_response_types(id=2):
    response = requests.get(BASE +"/sensordata/"+str(id), headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert type(response_content["id"]) == int
    assert type(response_content["temperature"]) == int
    assert type(datetime.datetime.strptime(response_content["measurement_datetime"],'%a, %d %b %Y %X %z')) == datetime.datetime
    assert type(response_content["sensor_id"]) == int

@pytest.mark.run(order=1)
def test_GET_sensordata_response_id(id=2):
    response = requests.get(BASE +"/sensordata/"+str(id), headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    assert response_content["id"] == id

