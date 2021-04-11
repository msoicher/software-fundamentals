from test_helper import *
from data_file import users
import json

def auth_register():

    email = input("email: ")
    name_first = input("first: ")
    name_last = input("last: ")
    password = input("password: ")

    if invalid_email(email):
        raise InputError(f"The email '{email}' does not meet the format requirements")

    elif invalid_password(password):
        raise InputError(f"The password '{password}' is less than 6 characters")

    elif invalid_name(name_first):
        raise InputError(f"Your first name '{name_first}' has to be at least 1 character and up to 50")

    elif invalid_name(name_last):
        raise InputError(f"Your last name '{name_first}' has to be at least 1 character and up to 50")

    elif email_exists(email):
        raise InputError(f"The email '{email}' is already in use. Please register using a different email")

    else:
        result = add_user(email, password, name_first, name_last)
        return result

auth_register()
print(json.dumps(users, indent=4))
