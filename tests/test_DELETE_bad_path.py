import random

import requests
import json
import pytest
from api.auth_headers import correct_header_1

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
@pytest.mark.run(order=5)
def test_response_code():
    response = requests.delete(BASE +"/town/"+del_id(), headers=correct_header_1)
    assert response.status_code==404