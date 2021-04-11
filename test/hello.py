from data_file import users
import json
import copy as cp

email = 'first@email.com'



firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
handle = firstName + lastName

add_new_user = False

if add_new_user:
    users[len(users) + 1] = key

print(json.dumps(users, indent=4))
