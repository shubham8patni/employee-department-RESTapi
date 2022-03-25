import requests

api_url = "http://employee-department-restapi.herokuapp.com/department/q=todo"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print(response.json())
