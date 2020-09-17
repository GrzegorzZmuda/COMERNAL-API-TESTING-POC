import datetime
import requests
import json
import random
from auth_headers import correct_header_1, incorrect_header_1
import pytest
BASE = "http://127.0.0.1:5000/"

namelist=["ga","pa","na","za","ka","la","ke","ze","de","ne","ko","ro","do","mo"]



def random_cityname():
    ln=random.randrange(2,5)
    str=""
    for i in range(ln):
        str=str+namelist[random.randrange(0,len(namelist))]
    return str

def gen_body_full():
    dict={"cityname": random_cityname(), "inhabitants": random.randrange(1000,10000)}
    return dict
@pytest.mark.run(order=1)
def test_response_code():
    response = requests.post(BASE +"/town",gen_body_full() ,headers=correct_header_1)
    assert response.status_code==404
@pytest.mark.run(order=1)
def test_response_code_unauth():
    response = requests.post(BASE +"/town",gen_body_full() ,headers=incorrect_header_1)
    assert response.status_code==404
@pytest.mark.run(order=1)
def test_response_code_no_auth():
    response = requests.post(BASE +"/town",gen_body_full() )
    assert response.status_code==404


