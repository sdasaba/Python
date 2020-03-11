import json

userJSON = '{"first_name": "LEE", "last_name": "WANGI", "age": 35}'

user = json.loads(userJSON)
print(user)