import requests
import json

base_url = "https://api.kandy.io/v1.2/"

def http_get(url):
    req = requests.get(url)
    data = req.json()
    return data
    
def http_post_json(url, payload):
    data = None
    if payload:
        data = json.dumps(payload)
    headers = {
        "Content-Type":"application/json"
    }
    req = requests.post(url, headers=headers, data=data)
    data = req.json()
    return data
    
def http_delete(url):
    req = requests.get(url)
    data = req.json()
    return data
