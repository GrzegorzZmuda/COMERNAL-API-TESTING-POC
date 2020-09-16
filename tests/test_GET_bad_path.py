import requests
from auth_headers import correct_header_1,incorrect_header_1

BASE = "http://127.0.0.1:5000/"

def del_id():
    return str(1)


def test_response_code_no_auth(id=2):
    response = requests.get(BASE +"/town/"+str(id))
    assert response.status_code==404

def test_response_code_unauth(id=2):
    response = requests.get(BASE +"/town/"+str(id), headers=incorrect_header_1)
    assert response.status_code==404


def test_response_code_not_found(id=999999):
    response = requests.get(BASE +"/town/"+str(id), headers=correct_header_1)
    assert response.status_code==404

def test_response_code_sensordata():
    response = requests.delete(BASE +"/sensrodata/"+del_id(), headers=correct_header_1)
    assert response.status_code==404

def test_response_code_sensor():
    response = requests.delete(BASE +"/sensor/"+del_id(), headers=correct_header_1)
    assert response.status_code==404

def test_response_code_city():
    response = requests.delete(BASE +"/city/"+del_id(), headers=correct_header_1)
    assert response.status_code==404