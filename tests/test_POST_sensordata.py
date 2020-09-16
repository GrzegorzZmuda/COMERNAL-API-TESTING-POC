import datetime
import time
import requests
import json
import random
from auth_headers import correct_header_1, incorrect_header_1

BASE = "http://127.0.0.1:5000/"

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
        "sensor_id": sensors_list[random.randrange(sensors_list_len)]
    }
    return dict

def gen_sensordata_full_without_date():
    dict={
        "temperature": random.randrange(1,70),
        "sensor_id": sensors_list[random.randrange(sensors_list_len)]
    }
    return dict

def gen_sensordata_without_temperature():
    dict={
        "measurement_datetime": datetime.datetime.isoformat(
            datetime.datetime.now() - datetime.timedelta(seconds=random.randrange(0, 100000000))),
        "sensor_id": sensors_list[random.randrange(sensors_list_len)]
    }
    return dict

def gen_sensordata_sensot_not_exist():
    dict={
        "temperature": random.randrange(1,70),
        "measurement_datetime": datetime.datetime.isoformat(datetime.datetime.now()- datetime.timedelta(seconds=random.randrange(0,100000000))),
        "sensor_id": max(sensors_list)+20
    }
    return dict



def test_response_code():
    response = requests.post(BASE +"/sensordata",gen_sensordata_full() ,headers=correct_header_1)
    assert response.status_code==201

def test_response_code_without_date():
    response = requests.post(BASE +"/sensordata",gen_sensordata_full_without_date() ,headers=correct_header_1)
    assert response.status_code==201

def test_response_code_without_temperature():
    response = requests.post(BASE +"/sensordata",gen_sensordata_without_temperature() ,headers=correct_header_1)
    assert response.status_code==400

def test_response_code_no_auth():
    response = requests.post(BASE +"/sensordata",gen_sensordata_full() )
    assert response.status_code==401

def test_response_code_unauth():
    response = requests.post(BASE +"/sensordata",gen_sensordata_full() ,headers=incorrect_header_1)
    assert response.status_code==401

def test_response_code_no_sensor():
    response = requests.post(BASE +"/sensordata",gen_sensordata_sensot_not_exist() ,headers=correct_header_1)
    assert response.status_code==404



def test_response_content():
    response = requests.post(BASE +"/sensordata",gen_sensordata_full() ,headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'

def test_response_content_without_date():
    response = requests.post(BASE +"/sensordata",gen_sensordata_full_without_date() ,headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'

def test_response_content_without_temperature():
    response = requests.post(BASE +"/sensordata",gen_sensordata_without_temperature() ,headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'

def test_response_content_no_auth():
    response = requests.post(BASE +"/sensordata",gen_sensordata_full() )
    assert  'text/html' in response.headers.get('content-type')

def test_response_content_unauth():
    response = requests.post(BASE +"/sensordata",gen_sensordata_full() ,headers=incorrect_header_1)
    assert  'text/html' in response.headers.get('content-type')

def test_response_content_no_sensor():
    response = requests.post(BASE +"/sensordata",gen_sensordata_sensot_not_exist() ,headers=correct_header_1)
    assert  'application/json' in response.headers.get('content-type')



def test_response_content_msg():
    a=gen_sensordata_full()
    response = requests.post(BASE +"/sensordata",a,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["temperature"] == a["temperature"]
    assert response_content["measurement_datetime"],'%a, %d %b %Y %X %z' == a["measurement_datetime"]
    assert response_content["sensor_id"] == a["sensor_id"]

def test_response_content_msg_without_date():
    a =gen_sensordata_full_without_date()
    response = requests.post(BASE +"/sensordata",a ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["temperature"] == a["temperature"]
    assert response_content["sensor_id"] == a["sensor_id"]

def test_response_content_msg_without_temperature():
    response = requests.post(BASE +"/sensordata",gen_sensordata_without_temperature() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"]["temperature"]== "measured temperature is required"

def test_response_content_msg_no_auth():
    response = requests.post(BASE +"/sensordata",gen_sensordata_full() )
    response_content = response.content.decode()
    assert response_content=="Unauthorised"

def test_response_content_msg_unauth():
    response = requests.post(BASE +"/sensordata",gen_sensordata_full() ,headers=incorrect_header_1)
    response_content = response.content.decode()
    assert response_content=="Unauthorised"

def test_response_content_msg_no_sensor():
    response = requests.post(BASE +"/sensordata",gen_sensordata_sensot_not_exist() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"] == "could not find sensor with that id"










def test_response_content_msg_type():
    response = requests.post(BASE + "/sensordata", gen_sensordata_full(), headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content["id"]) == int
    assert type(response_content["temperature"]) == int
    assert type(
        datetime.datetime.strptime(response_content["measurement_datetime"], '%a, %d %b %Y %X %z')) == datetime.datetime
    assert type(response_content["sensor_id"]) == int


def test_response_content_msg_type_without_date():
    response = requests.post(BASE + "/sensordata", gen_sensordata_full_without_date(), headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content["id"]) == int
    assert type(response_content["temperature"]) == int
    assert type(
        datetime.datetime.strptime(response_content["measurement_datetime"], '%a, %d %b %Y %X %z')) == datetime.datetime
    assert type(response_content["sensor_id"]) == int

def test_response_content_msg_type_without_temperature():
    response = requests.post(BASE +"/sensordata",gen_sensordata_without_temperature() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content["message"]["temperature"])== str

def test_response_content_msg_type_no_auth():
    response = requests.post(BASE +"/sensordata",gen_sensordata_full() )
    response_content = response.content.decode()
    assert type(response_content)==str

def test_response_content_msg_type_unauth():
    response = requests.post(BASE +"/sensordata",gen_sensordata_full() ,headers=incorrect_header_1)
    response_content = response.content.decode()
    assert type(response_content)==str

def test_response_content_msg_type_no_sensor():
    response = requests.post(BASE +"/sensordata",gen_sensordata_sensot_not_exist() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content["message"]) ==str


def test_response_code_empty_temperature_field():
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}
    temp = str({'temperature': 37, 'sensor_id': 108}).replace("\'", "\"")
    reqstr = temp[0:15] + temp[18:]


    response = requests.post(BASE +"/sensordata",data=reqstr,headers=correct_header_1_upg)
    response_content = json.loads(response.content.decode())

    assert response.status_code==400

def test_response_msg_type_empty_temperature_field():
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}
    temp = str({'temperature': 37, 'sensor_id': 108}).replace("\'", "\"")
    reqstr = temp[0:15] + temp[18:]


    response = requests.post(BASE +"/sensordata",data=reqstr,headers=correct_header_1_upg)
    response_content = json.loads(response.content.decode())

    assert type(response_content["message"]) == str

def test_response_msg_empty_temperature_field():
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}
    temp = str({'temperature': 37, 'sensor_id': 108}).replace("\'", "\"")
    reqstr = temp[0:15] + temp[18:]


    response = requests.post(BASE +"/sensordata",data=reqstr,headers=correct_header_1_upg)
    response_content = json.loads(response.content.decode())

    assert "Failed to decode JSON object: " in response_content["message"]
