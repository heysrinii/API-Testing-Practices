import requests
import json

# API URL
base_url = "https://reqres.in/api/users?page=2"

# Create GET
response = requests.get(base_url, json_request)
print(response.content)
