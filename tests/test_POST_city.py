c=":"
import requests
import json
import random
import pytest
from API.auth_headers import correct_header_1

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

def gen_body_full_str_as_inhabitants():
    dict={"cityname": random_cityname(), "inhabitants": "strrr"}
    return dict

def gen_body_cityname():
    dict={"cityname": random_cityname()}
    return dict

def gen_body_inhabitants():
    dict={ "inhabitants": random.randrange(1000,10000)}
    return dict

def gen_body_empty():
    dict={}
    return dict



@pytest.mark.run(order=1)
def test_response_code():
    response = requests.post(BASE +"/city",gen_body_full() ,headers=correct_header_1)
    assert response.status_code==201
@pytest.mark.run(order=1)
def test_response_code_no_cityname():
    response = requests.post(BASE +"/city",gen_body_inhabitants() ,headers=correct_header_1)
    assert response.status_code==400
@pytest.mark.run(order=1)
def test_response_code_no_inhabitants():
    response = requests.post(BASE +"/city",gen_body_cityname() ,headers=correct_header_1)
    assert response.status_code==400
@pytest.mark.run(order=1)
def test_response_code_empty_body():
    response = requests.post(BASE +"/city",gen_body_empty() ,headers=correct_header_1)
    assert response.status_code==400
@pytest.mark.run(order=1)
def test_response_code_str_as_inhabitants():
    response = requests.post(BASE + "/city", gen_body_full_str_as_inhabitants(), headers=correct_header_1)
    assert response.status_code == 400

@pytest.mark.run(order=1)
def test_response_content():
    response = requests.post(BASE +"/city",gen_body_full() ,headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'
@pytest.mark.run(order=1)
def test_response_content_no_cityname():
    response = requests.post(BASE +"/city",gen_body_inhabitants() ,headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'
@pytest.mark.run(order=1)
def test_response_content_no_inhabitants():
    response = requests.post(BASE +"/city",gen_body_cityname() ,headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'
@pytest.mark.run(order=1)
def test_response_content_empty_body():
    response = requests.post(BASE +"/city",gen_body_empty() ,headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'
@pytest.mark.run(order=1)
def test_response_content_str_as_inhabitants():
    response = requests.post(BASE +"/city",gen_body_full_str_as_inhabitants() ,headers=correct_header_1)
    assert response.headers.get('content-type') == 'application/json'

@pytest.mark.run(order=1)
def test_response_inside_content():
    generated = gen_body_full()
    response = requests.post(BASE +"/city",generated ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["cityname"] == generated["cityname"]
    assert response_content["inhabitants"] == generated["inhabitants"]
    assert type(response_content["id"]) == int
@pytest.mark.run(order=1)
def test_response_inside_content_no_cityname():
    response = requests.post(BASE +"/city",gen_body_inhabitants() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"] != None
@pytest.mark.run(order=1)
def test_response_inside_content_no_inhabitants():
    response = requests.post(BASE +"/city",gen_body_cityname() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"] != None
@pytest.mark.run(order=1)
def test_response_inside_content_empty_body():
    response = requests.post(BASE +"/city",gen_body_empty() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"] != None
@pytest.mark.run(order=1)
def test_response_inside_content_str_as_inhabitants():
    response = requests.post(BASE +"/city",gen_body_full_str_as_inhabitants() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"] != None

@pytest.mark.run(order=1)
def test_response_inside_content_correct_message_type_no_cityname():
    response = requests.post(BASE +"/city",gen_body_inhabitants() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content["message"]["cityname"]) == str
@pytest.mark.run(order=1)
def test_response_inside_content_correct_message_type_no_inhabitants():
    response = requests.post(BASE +"/city",gen_body_cityname() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content["message"]["inhabitants"]) == str
@pytest.mark.run(order=1)
def test_response_inside_content_correct_message_type_empty_body():
    response = requests.post(BASE +"/city",gen_body_empty() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert type(response_content["message"]["cityname"]) == str
@pytest.mark.run(order=1)
def test_response_inside_content_correct_message_type_str_as_inhabitants():
    response = requests.post(BASE +"/city",gen_body_full_str_as_inhabitants() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    print(response_content["message"])
    assert type(response_content["message"]["inhabitants"]) == str
@pytest.mark.run(order=1)
def test_response_inside_content_correct_message_no_cityname():
    response = requests.post(BASE +"/city",gen_body_inhabitants() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"]["cityname"] == "Name of the city is required"
@pytest.mark.run(order=1)
def test_response_inside_content_correct_message_no_inhabitants():
    response = requests.post(BASE +"/city",gen_body_cityname() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"]["inhabitants"] == "Number of inhabitants required"
@pytest.mark.run(order=1)
def test_response_inside_content_correct_message_empty_body():
    response = requests.post(BASE +"/city",gen_body_empty() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    assert response_content["message"]["cityname"] == "Name of the city is required"
@pytest.mark.run(order=1)
def test_response_inside_content_correct_message_str_as_inhabitants():
    response = requests.post(BASE +"/city",gen_body_full_str_as_inhabitants() ,headers=correct_header_1)
    response_content = json.loads(response.content.decode())
    print(response_content["message"])
    assert response_content["message"]["inhabitants"] == "Number of inhabitants required"

@pytest.mark.run(order=1)
def test_response_inside_content_correct_message_empty_inhabitants_field():
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}


    temp=str({"cityname": "nadezane", "inhabitants": 5274}).replace("\'","\"")
    reqstr=temp[0:40]+temp[-1]
    response = requests.post(BASE +"/city",data=reqstr,headers=correct_header_1_upg)
    response_content = json.loads(response.content.decode())
    print(response_content)
    assert "Failed to decode JSON object:" in response_content["message"]

@pytest.mark.run(order=1)
def test_response_inside_content_correct_message_type_empty_inhabitants_field():
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}


    temp=str({"cityname": "nadezane", "inhabitants": 5274}).replace("\'","\"")
    reqstr=temp[0:40]+temp[-1]
    response = requests.post(BASE +"/city",data=reqstr,headers=correct_header_1_upg)
    response_content = json.loads(response.content.decode())
    print(response_content)
    assert  type(response_content["message"]) == str
@pytest.mark.run(order=1)
def test_response_code_empty_inhabitants_field():
    correct_header_1_upg = {'Authorization': correct_header_1['Authorization'], 'Content-Type': 'application/json'}


    temp=str({"cityname": "nadezane", "inhabitants": 5274}).replace("\'","\"")
    reqstr=temp[0:40]+temp[-1]
    response = requests.post(BASE +"/city",data=reqstr,headers=correct_header_1_upg)
    response_content = json.loads(response.content.decode())
    assert response.status_code==400

