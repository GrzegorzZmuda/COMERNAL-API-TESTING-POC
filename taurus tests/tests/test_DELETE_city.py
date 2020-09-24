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

def get_cities_ids():
    response = requests.get(BASE +"/city", headers=correct_header_1)
    response_content=json.loads(response.content.decode())
    ls=[]
    for i in range(len(response_content)):
        if response_content[i]["id"]>2:
            ls.append(response_content[i]["id"])

    return ls

def del_id():
    a  = get_cities_ids()
    return str(a[random.randrange(len(a))])
@pytest.mark.run(order=5)
def test_DELETE_city_response_code():
    response = requests.delete(BASE +"/city/"+del_id(), headers=correct_header_1)
    assert response.status_code==204
@pytest.mark.run(order=5)
def test_DELETE_city_response_code_no_auth():
    response = requests.delete(BASE +"/city/"+del_id())
    assert response.status_code==401
@pytest.mark.run(order=5)
def test_DELETE_city_response_code_unauth():
    response = requests.delete(BASE +"/city/"+del_id(), headers=incorrect_header_1)
    assert response.status_code==401