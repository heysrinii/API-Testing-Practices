import requests
import json
import jsonpath

# API URL
base_url = "https://reqres.in/api/users/2"

# Read Input From Json File
file = open('/home/srinii/PycharmProjects/Excersise/Users.json')
json_input = file.read()
json_request = json.loads(json_input)
#print(json_request)

# Create PUT
response = requests.put(base_url, json_request)
#print(response.content)

assert response.status_code == 200

#Fetch Header from Response
#print(response.headers.get('Content-Length'))

#Parse response to Json format
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])
