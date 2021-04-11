import re
from data_file import users



def add_user(email, password, name_first, name_last):

    u_id = len(users) + 1 # id's are allocated simply by the data's key size, incremented each time
    token = u_id
    handle = create_handle(name_first, name_last, u_id)
    name = name_first + ' ' + name_last

    key = {
        'email': email,
        'password': password,
        'name': name,
        'handle': handle
    }

    users[u_id] = key
    # token for now is u_id, subject to change
    return { u_id, token }

# check that the password matches the email when logging in
def wrong_password(email, password):

    for user in dict(users).values():
        if user['password'] == password:
            return False

    return True


def find_u_id(email):

    for u_id, user in dict(users).items():
        if user['email'] == email:
            return u_id


def email_exists(email):

    for user in dict(users).values():
        if user['email'] == email:
            return True

    return False


def invalid_email(email):

# sourced from https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    # if the below is true, our email is VALID, thus we return FALSE
    if re.search(regex, email):
        return False

    return True


def invalid_name(name):

    if len(name) < 1 or len(name) > 50:
        return True

    return False


def invalid_password(password):

    if len(password) < 6:
        return True

    return False


# by creating a handle including the u_id below, handles are guaranteed to be unique
def create_handle(name_first, name_last, u_id):

    first = name_first.lower()
    last = name_last.lower()
    full_name = first + last
    u_id = str(u_id)

    # if the user's first and last name + u_id e.g. John Smith 1, can create a
    # handle johnsmith1 which is 20 chars of less, create that handle

    if len(full_name + u_id) < 21:
        handle = full_name + u_id

    # If the above case fails, use first letter of first name + last name  + u_id
    elif len(first[0] + last + u_id) < 21:
        handle = first[0] + last + u_id

    # otherwise, handle is initials + unique u_id
    else:
        handle = first[0] + last[0] + u_id

    return handle
