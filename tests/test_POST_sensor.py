import datetime
import requests
import json
import random
from auth_headers import correct_header_1, incorrect_header_1

BASE = "http://127.0.0.1:5000/"

def get_cities_ids():
    response = requests.get(BASE +"/city", headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    ls=[]
    for i in range(len(response_content)):
        ls.append(response_content[i]["id"])
    return ls
cities_list=get_cities_ids()
cities_list_len=len(cities_list)

print(get_cities_ids())

def gen_sensor_full():
    dict={
        "height": random.randrange(1,70),
        "latitude": random.randrange(-90000,90000)/1000,
        "longitude": random.randrange(-180000,180000)/1000,
        "city_id": cities_list[random.randrange(cities_list_len)]
    }
    return dict

def gen_sensor_no_longitude():
    dict={
        "height": random.randrange(1,70),
        "latitude": random.randrange(-90000,90000)/1000,
        "city_id": cities_list[random.randrange(cities_list_len)]
    }
    return dict

def gen_sensor_city_not_exist():
    dict={
        "height": random.randrange(1,70),
        "latitude": random.randrange(-90000,90000)/1000,
        "longitude": random.randrange(-180000,180000)/1000,
        "city_id": max(cities_list)+12
    }
    return dict
#responses
def test_response_code():
    response = requests.post(BASE +"/sensor",gen_sensor_full() ,headers=correct_header_1)
    assert response.status_code==201

def test_response_code_no_longitude():
    response = requests.post(BASE +"/sensor",gen_sensor_no_longitude() ,headers=correct_header_1)
    assert response.status_code==400

def test_response_code_wrong_city_id():
    response = requests.post(BASE +"/sensor",gen_sensor_city_not_exist() ,headers=correct_header_1)
    assert response.status_code==404

def test_response_code_unauth():
    response = requests.post(BASE +"/sensor",gen_sensor_full() ,headers=incorrect_header_1)
    assert response.status_code==401

def test_response_code_no_auth():
    response = requests.post(BASE +"/sensor",gen_sensor_full() )
    assert response.status_code==401

#content header
def test_response_content():
    response = requests.post(BASE + "/sensor", gen_sensor_full(), headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'

def test_response_cotent_no_longitude():
    response = requests.post(BASE + "/sensor", gen_sensor_no_longitude(), headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'

def test_response_cotent_wrong_city_id():
    response = requests.post(BASE + "/sensor", gen_sensor_city_not_exist(), headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'

def test_response_cotent_unauth():
    response = requests.post(BASE + "/sensor", gen_sensor_full(), headers=incorrect_header_1)
    assert  'text/html' in response.headers.get('content-type')


def test_response_cotent_no_auth():
    response = requests.post(BASE + "/sensor", gen_sensor_full())
    assert 'text/html' in response.headers.get('content-type')

#content type
def test_response_content_type():
    response = requests.post(BASE +"/sensor",gen_sensor_full() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content)==dict

def test_response_cotent_type_no_longitude():
    response = requests.post(BASE +"/sensor",gen_sensor_no_longitude() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content)==dict

def test_response_cotent_type_wrong_city_id():
    response = requests.post(BASE +"/sensor",gen_sensor_city_not_exist() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content)==dict

def test_response_cotent_type_unauth():
    response = requests.post(BASE +"/sensor",gen_sensor_full() ,headers=incorrect_header_1)
    response_content = response.content.decode()
    assert type(response_content)==str

def test_response_cotent_type_no_auth():
    response = requests.post(BASE +"/sensor",gen_sensor_full() )
    response_content = response.content.decode()
    assert type(response_content)==str


#messenge
def test_response_cotent_msg_unauth():
    response = requests.post(BASE +"/sensor",gen_sensor_full() ,headers=incorrect_header_1)
    response_content = response.content.decode()
    assert response_content=="Unauthorised"

def test_response_cotent_msg_no_auth():
    response = requests.post(BASE +"/sensor",gen_sensor_full() )
    response_content = response.content.decode()
    assert response_content=="Unauthorised"

def test_response_cotent_msg_no_longitude():
    response = requests.post(BASE +"/sensor",gen_sensor_no_longitude() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"]["longitude"]== "Longitude of the sensor is required"

def test_response_cotent_msg_wrong_city_id():
    response = requests.post(BASE +"/sensor",gen_sensor_city_not_exist() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"]== "could not find city with that id"

def test_response_cotent_correct_check_types():
    response = requests.post(BASE +"/sensor",gen_sensor_full() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content["id"])== int
    assert type(response_content["height"]) == int
    assert type(response_content["latitude"]) == float
    assert type(response_content["longitude"]) == float
    assert type(response_content["city_id"]) == int

def test_response_cotent_correct():
    a=gen_sensor_full()
    response = requests.post(BASE +"/sensor",a ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["height"] == a["height"]
    assert response_content["latitude"]== a["latitude"]
    assert response_content["longitude"] == a["longitude"]
    assert response_content["city_id"] == a["city_id"]

def test_response_code_empty_height_field():
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}
    temp = str({'height': 30, 'latitude': -1.622, 'longitude': 99.369, 'city_id': 106}).replace("\'", "\"")
    reqstr = temp[0:8] + temp[15:]


    response = requests.post(BASE +"/sensor",data=reqstr,headers=correct_header_1_upg)
    response_content = json.loads(response.content.decode())
    print(response_content)
    assert response.status_code==400

def test_response_msg_type_empty_height_field():
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}
    temp = str({'height': 30, 'latitude': -1.622, 'longitude': 99.369, 'city_id': 106}).replace("\'", "\"")
    reqstr = temp[0:8] + temp[15:]


    response = requests.post(BASE +"/sensor",data=reqstr,headers=correct_header_1_upg)
    response_content = json.loads(response.content.decode())
    print(reqstr)
    assert type(response_content["message"]) == str

def test_response_msg_empty_height_field():
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}
    temp = str({'height': 30, 'latitude': -1.622, 'longitude': 99.369, 'city_id': 106}).replace("\'", "\"")
    reqstr = temp[0:8] + temp[15:]


    response = requests.post(BASE +"/sensor",data=reqstr,headers=correct_header_1_upg)
    response_content = json.loads(response.content.decode())
    print(response_content)
    assert "Failed to decode JSON object: " in response_content["message"]