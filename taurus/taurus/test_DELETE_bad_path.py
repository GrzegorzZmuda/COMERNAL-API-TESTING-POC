import random

import requests
import json
import pytest
from base64 import b64encode

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

BASE = "http://127.0.0.1:5000/"

BASE = "http://127.0.0.1:5000/"
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

def test_DELETE_bda_path_response_code():
    response = requests.delete(BASE +"/town/"+del_id(), headers=correct_header_1)
    assert response.status_code==404