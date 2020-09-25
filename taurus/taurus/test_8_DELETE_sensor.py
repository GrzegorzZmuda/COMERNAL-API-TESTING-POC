import random
import pytest
import requests
import json
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

def get_sensors_ids():
    response = requests.get(BASE +"/sensor", headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    ls=[]
    for i in range(len(response_content)):
        if response_content[i]["id"]>5:
            ls.append(response_content[i]["id"])
    return ls


def del_id():
    a  = get_sensors_ids()
    return str(a[random.randrange(len(a))])

def test_DELETE_sensor_response_code():
    response = requests.delete(BASE +"/sensor/"+del_id(), headers=correct_header_1)
    assert response.status_code==204

def test_DELETE_sensor_response_code_no_auth():
    response = requests.delete(BASE +"/sensor/"+del_id())
    assert response.status_code==401

def test_DELETE_sensor_response_code_unauth():
    response = requests.delete(BASE +"/sensor/"+del_id(), headers=incorrect_header_1)
    assert response.status_code==401