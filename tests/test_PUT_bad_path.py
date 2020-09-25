import random

import pytest
import requests

from api.auth_headers import correct_header_1

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

@pytest.mark.run(order=2)
def test_response_code(id=2):
    response = requests.put(BASE +"/town/"+str(id),gen_body_full() ,headers=correct_header_1)
    assert response.status_code==404