import requests
response = requests.get('https://pudim.com.br/')
print(response.status_code) 