import requests
res = requests.post('http://203.246.112.75:8000/api/token-auth/', 
                    data={'username': 'drone_admin',
                          'password': 'midrone2023@'}).json()
token = res['token']
print(token)