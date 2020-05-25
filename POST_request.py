import requests
import json

# API URL
base_url = "https://reqres.in/api/users/"

# Read Input From Json File
file = open('/home/srinii/PycharmProjects/Excersise/Users.json')
json_input = file.read()
json_request = json.loads(json_input)
#print(json_request)

# Create POST
response = requests.post(base_url, json_request)
print(response.content)
