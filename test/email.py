import re
# sourced from https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
email = 'email@gmail.com'
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

if re.search(regex, email):
    print('Email is correct')
else:
    print('Email is not correct')
