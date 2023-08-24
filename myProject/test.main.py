import json
import requests



BASE_URL = "https://system-service-rubenpinxten.cloud.okteto.net"

def create_testadmin():
    adminexists = requests.get(f'{BASE_URL}/admin/admintest')
    if adminexists:
        print("INFO: Test admin already exists!")
    else:
        username = "admintest"
        password = "admintest"
        data = json.dumps({"username": username, "password": password})
        requests.post(f'{BASE_URL}/admin', data=data)

headers = {
"Content-Type": "application/x-www-form-urlencoded"
}

request_data = {
    "client_id": "",
    "client_secret": "",
    "scope": "",
    "grant_type": "",
    "refresh_token": "",
    "username": "admintest",
    "password": "admintest"
}