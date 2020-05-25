import requests

headersdata = {'T1': 'First_Header', 'T2': 'Second_Header'}
response = requests.get("https://httpbin.org/get", headers=headersdata)
print(response.text)
