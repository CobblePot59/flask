import requests

url = 'http://localhost/login'
creds = {'login': 'admin', 'password': 'admin'}
s = requests.Session()

# Authenticate and get the token
response = s.post(url, json=creds)
token = response.json()['token']
print(token)

# Pass the token with the request
url = 'http://localhost/protected'
headers = {'Authorization': 'Bearer ' + token}
r = s.get(url, headers=headers)
print(r.text)
