# API documentations
# https://todo.pixegami.io/docs

import requests


endPoint="https://todo.pixegami.io/"

response=requests.get(endPoint)
print(response)    #---><Response [200]>

# to get json object out of response
data=response.json()
print(data)       #--->{'message': 'Hello World from Todo API'}
print(data['message'])

'''
print(data['task'])
for key in data['task']:
    print(f"{key}:{data['task'][key]}")
'''

# to get only status code
status_code=response.status_code
print(status_code)



