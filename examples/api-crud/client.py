import requests


url = 'http://localhost/login'
creds = {'login': 'admin', 'password': 'admin'}
s = requests.Session()

# Authenticate and get the access token
response = s.post(url, json=creds)
token = response.json()['token']
headers = {'Authorization': 'Bearer ' + token}


# Pass the access token with the request

# Get all users
# url = 'http://localhost/users'
# r = s.get(url, headers=headers)
# print(r.text)

# Get specific user
# url = 'http://localhost/users/1'
# r = s.get(url, headers=headers)
# print(r.text)

# Add an user
# url = 'http://localhost/users'
# data = {'email': 'user3@example.com', 'username': 'user3', 'password': 'user3'}
# r = s.post(url, headers=headers, json=data)
# print(r.text)

# Edit an user
# url = 'http://localhost/users/3'
# data = {'email': 'user4@example.com', 'username': 'user4', 'password': 'user4'}
# r = s.put(url, headers=headers, json=data)
# print(r.text)

# Delete an user
# url = 'http://localhost/users/4'
# r = s.delete(url, headers=headers)
# print(r.text)

# Get all users
url = 'http://localhost/users'
r = s.get(url, headers=headers)
print(r.text)