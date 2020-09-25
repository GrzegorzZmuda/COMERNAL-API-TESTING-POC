

import datetime
import requests
import json
import random
from base64 import b64encode
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


def get_sensors_ids():
    response = requests.get(BASE +"/sensor", headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    ls=[]
    for i in range(len(response_content)):
        ls.append(response_content[i]["id"])
    return ls
sensors_list=get_sensors_ids()
sensors_list_len=len(sensors_list)


def gen_sensordata_full():
    dict={
        "temperature": random.randrange(1,70),
        "measurement_datetime": datetime.datetime.isoformat(datetime.datetime.now()- datetime.timedelta(seconds=random.randrange(0,100000000))),
        "sensor_id": 2
    }
    return dict

def gen_sensordata_full_without_date():
    dict={
        "temperature": random.randrange(1,70),
        "sensor_id": 2
    }
    return dict

def gen_sensordata_without_temperature():
    dict={
        "measurement_datetime": datetime.datetime.isoformat(
            datetime.datetime.now() - datetime.timedelta(seconds=random.randrange(0, 100000000))),
        "sensor_id": 2
    }
    return dict

def gen_sensordata_sensot_not_exist():
    dict={
        "temperature": random.randrange(1,70),
        "measurement_datetime": datetime.datetime.isoformat(datetime.datetime.now()- datetime.timedelta(seconds=random.randrange(0,100000000))),
        "sensor_id": max(sensors_list)+202222
    }
    return dict



def test_PUT_sensordata_response_code(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_full() ,headers=correct_header_1)
    assert response.status_code==200

def test_PUT_sensordata_response_code_without_date(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_full_without_date() ,headers=correct_header_1)
    assert response.status_code==200

def test_PUT_sensordata_response_code_without_temperature(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_without_temperature() ,headers=correct_header_1)
    assert response.status_code==200

def test_PUT_sensordata_response_code_no_auth(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_full() )
    assert response.status_code==401

def test_PUT_sensordata_response_code_unauth(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_full() ,headers=incorrect_header_1)
    assert response.status_code==401

def test_PUT_sensordata_response_code_no_sensor(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_sensot_not_exist() ,headers=correct_header_1)
    assert response.status_code==404



def test_PUT_sensordata_response_content(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_full() ,headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'

def test_PUT_sensordata_response_content_without_date(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_full_without_date() ,headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'

def test_PUT_sensordata_response_content_without_temperature(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_without_temperature() ,headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'

def test_PUT_sensordata_response_content_no_auth(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_full() )
    assert  'text/html' in response.headers.get('content-type')

def test_PUT_sensordata_response_content_unauth(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_full() ,headers=incorrect_header_1)
    assert  'text/html' in response.headers.get('content-type')

def test_PUT_sensordata_response_content_no_sensor(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_sensot_not_exist() ,headers=correct_header_1)
    assert  'application/json' in response.headers.get('content-type')



def test_PUT_sensordata_response_content_msg(id=2):
    a=gen_sensordata_full()
    response = requests.put(BASE +"/sensordata/"+str(id),a,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["temperature"] == a["temperature"]
    assert response_content["measurement_datetime"],'%a, %d %b %Y %X %z' == a["measurement_datetime"]
    assert response_content["sensor_id"] == a["sensor_id"]

def test_PUT_sensordata_response_content_msg_without_date(id=2):
    a =gen_sensordata_full_without_date()
    response = requests.put(BASE +"/sensordata/"+str(id),a ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["temperature"] == a["temperature"]
    assert response_content["sensor_id"] == a["sensor_id"]


def test_PUT_sensordata_response_content_msg_no_auth(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_full() )
    response_content = response.content.decode()
    assert response_content=="Unauthorised"

def test_PUT_sensordata_response_content_msg_unauth(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_full() ,headers=incorrect_header_1)
    response_content = response.content.decode()
    assert response_content=="Unauthorised"

def test_PUT_sensordata_response_content_msg_no_sensor(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_sensot_not_exist() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"] == "could not find sensor with that id"










def test_PUT_sensordata_response_content_msg_type(id=2):
    response = requests.put(BASE + "/sensordata/"+str(id), gen_sensordata_full(), headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content["id"]) == int
    assert type(response_content["temperature"]) == int
    assert type(
        datetime.datetime.strptime(response_content["measurement_datetime"], '%a, %d %b %Y %X %z')) == datetime.datetime
    assert type(response_content["sensor_id"]) == int


def test_PUT_sensordata_response_content_msg_type_without_date(id=2):
    response = requests.put(BASE + "/sensordata/"+str(id), gen_sensordata_full_without_date(), headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content["id"]) == int
    assert type(response_content["temperature"]) == int
    assert type(
        datetime.datetime.strptime(response_content["measurement_datetime"], '%a, %d %b %Y %X %z')) == datetime.datetime
    assert type(response_content["sensor_id"]) == int


def test_PUT_sensordata_response_content_msg_type_no_auth(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_full() )
    response_content = response.content.decode()
    assert type(response_content)==str

def test_PUT_sensordata_response_content_msg_type_unauth(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_full() ,headers=incorrect_header_1)
    response_content = response.content.decode()
    assert type(response_content)==str

def test_PUT_sensordata_response_content_msg_type_no_sensor(id=2):
    response = requests.put(BASE +"/sensordata/"+str(id),gen_sensordata_sensot_not_exist() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content["message"]) ==str


def test_PUT_sensordata_response_code_empty_temperature_field(id=2):
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}
    temp = str({'temperature': 37, 'sensor_id': 108}).replace("\'", "\"")
    reqstr = temp[0:15] + temp[18:]


    response = requests.put(BASE +"/sensordata/"+str(id),data=reqstr,headers=correct_header_1_upg)

    assert response.status_code==400

def test_PUT_sensordata_response_msg_type_empty_temperature_field(id=2):
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}
    temp = str({'temperature': 37, 'sensor_id': 108}).replace("\'", "\"")
    reqstr = temp[0:15] + temp[18:]


    response = requests.put(BASE +"/sensordata/"+str(id),data=reqstr,headers=correct_header_1_upg)
    response_content = json.loads(response.content.decode())

    assert type(response_content["message"]) == str

