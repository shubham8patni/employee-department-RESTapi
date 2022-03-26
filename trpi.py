import requests
import json
api_url = "http://employee-department-restapi.herokuapp.com/create"
create = {"userId": 1, "title": "Buy milk", "completed": False}
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(create), headers=headers)
print(response.json())
