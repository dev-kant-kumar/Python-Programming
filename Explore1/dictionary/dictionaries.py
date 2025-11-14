# dictionaries in python : a collection datatype use to store multiple element under single variable and it store elements as key value pair .

import time

last_login = time.time()

# creation of dictionary

user = {
    "user_name" : "devkantkumar",
    "role" : "admin",
    "__id" : "a08765esxcvbnmki765",
    "access_type" :"full_access",
    "is_on_subscription" : True,
    "last_login" : last_login
}

# print(f'user : {user}')

# accessing the elements of dictionary
# 1 method by key of dictionary
# print(f'user name : {user["user_name"]} have role of : {user["role"]} and last login on : {user["last_login"]}')

# 2 method bby get method
print(f'user name : {user.get("user_name")}')

# accessing the keys of dictionary

# keys = user.keys()
# print(f'keys are : {keys}')
