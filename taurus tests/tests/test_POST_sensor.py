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

def get_cities_ids():
    response = requests.get(BASE +"/city", headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    ls=[]
    for i in range(len(response_content)):
        ls.append(response_content[i]["id"])
    return ls
cities_list=get_cities_ids()
cities_list_len=len(cities_list)



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
@pytest.mark.run(order=1)
def test_POST_sensor_response_code():
    response = requests.post(BASE +"/sensor",gen_sensor_full() ,headers=correct_header_1)
    assert response.status_code==201
@pytest.mark.run(order=1)
def test_POST_sensor_response_code_no_longitude():
    response = requests.post(BASE +"/sensor",gen_sensor_no_longitude() ,headers=correct_header_1)
    assert response.status_code==400
@pytest.mark.run(order=1)
def test_POST_sensor_response_code_wrong_city_id():
    response = requests.post(BASE +"/sensor",gen_sensor_city_not_exist() ,headers=correct_header_1)
    assert response.status_code==404
@pytest.mark.run(order=1)
def test_POST_sensor_response_code_unauth():
    response = requests.post(BASE +"/sensor",gen_sensor_full() ,headers=incorrect_header_1)
    assert response.status_code==401
@pytest.mark.run(order=1)
def test_POST_sensor_response_code_no_auth():
    response = requests.post(BASE +"/sensor",gen_sensor_full() )
    assert response.status_code==401

#content header
@pytest.mark.run(order=1)
def test_POST_sensor_response_content():
    response = requests.post(BASE + "/sensor", gen_sensor_full(), headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_no_longitude():
    response = requests.post(BASE + "/sensor", gen_sensor_no_longitude(), headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_wrong_city_id():
    response = requests.post(BASE + "/sensor", gen_sensor_city_not_exist(), headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_unauth():
    response = requests.post(BASE + "/sensor", gen_sensor_full(), headers=incorrect_header_1)
    assert  'text/html' in response.headers.get('content-type')

@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_no_auth():
    response = requests.post(BASE + "/sensor", gen_sensor_full())
    assert 'text/html' in response.headers.get('content-type')

#content type
@pytest.mark.run(order=1)
def test_POST_sensor_response_content_type():
    response = requests.post(BASE +"/sensor",gen_sensor_full() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content)==dict
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_type_no_longitude():
    response = requests.post(BASE +"/sensor",gen_sensor_no_longitude() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content)==dict
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_type_wrong_city_id():
    response = requests.post(BASE +"/sensor",gen_sensor_city_not_exist() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content)==dict
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_type_unauth():
    response = requests.post(BASE +"/sensor",gen_sensor_full() ,headers=incorrect_header_1)
    response_content = response.content.decode()
    assert type(response_content)==str
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_type_no_auth():
    response = requests.post(BASE +"/sensor",gen_sensor_full() )
    response_content = response.content.decode()
    assert type(response_content)==str


#messenge
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_msg_unauth():
    response = requests.post(BASE +"/sensor",gen_sensor_full() ,headers=incorrect_header_1)
    response_content = response.content.decode()
    assert response_content=="Unauthorised"
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_msg_no_auth():
    response = requests.post(BASE +"/sensor",gen_sensor_full() )
    response_content = response.content.decode()
    assert response_content=="Unauthorised"
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_msg_no_longitude():
    response = requests.post(BASE +"/sensor",gen_sensor_no_longitude() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"]["longitude"]== "Longitude of the sensor is required"
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_msg_wrong_city_id():
    response = requests.post(BASE +"/sensor",gen_sensor_city_not_exist() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"]== "could not find city with that id"
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_correct_check_types():
    a=gen_sensor_full()
    response = requests.post(BASE +"/sensor",gen_sensor_full() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    print(a,response_content)
    assert type(response_content["id"])== int
    assert type(response_content["height"]) == int
    assert type(response_content["latitude"]) == float
    assert type(response_content["longitude"]) == float
    assert type(response_content["city_id"]) == int
@pytest.mark.run(order=1)
def test_POST_sensor_response_cotent_correct():
    a=gen_sensor_full()
    response = requests.post(BASE +"/sensor",a ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["height"] == a["height"]
    assert response_content["latitude"]== a["latitude"]
    assert response_content["longitude"] == a["longitude"]
    assert response_content["city_id"] == a["city_id"]
@pytest.mark.run(order=1)
def test_POST_sensor_response_code_empty_height_field():
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}
    temp = str({'height': 30, 'latitude': -1.622, 'longitude': 99.369, 'city_id': 106}).replace("\'", "\"")
    reqstr = temp[0:8] + temp[15:]


    response = requests.post(BASE +"/sensor",data=reqstr,headers=correct_header_1_upg)
    response_content = json.loads(response.content.decode())
    print(response_content)
    assert response.status_code==400
@pytest.mark.run(order=1)
def test_POST_sensor_response_msg_type_empty_height_field():
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}
    temp = str({'height': 30, 'latitude': -1.622, 'longitude': 99.369, 'city_id': 106}).replace("\'", "\"")
    reqstr = temp[0:8] + temp[15:]


    response = requests.post(BASE +"/sensor",data=reqstr,headers=correct_header_1_upg)
    response_content = json.loads(response.content.decode())
    print(reqstr)
    assert type(response_content["message"]) == str
