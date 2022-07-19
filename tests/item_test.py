from flask import Flask
import json
from app import app as api


def test_items():
    client = api.test_client()
    url = 'http://127.0.0.1:5000/items'
    
    response = client.get(url)
    my_json = json.loads(response.data)
    assert my_json[0]['name']=='debashish'
    assert my_json[0]['age']==20
    assert response.status_code == 200
    
    
    
def test_item():
    client = api.test_client()
    url = 'http://127.0.0.1:5000/item/debashish'
    
    response = client.get(url)
    my_json = json.loads(response.data)
    assert my_json['name']=='debashish'
    assert my_json['age']==20
    assert response.status_code == 200
    
    