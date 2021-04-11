users = {
    1: {
        'email': "first@email.com",
        'name': 'First User',
        'password': 'firstpassword',
        'handle': 'firstuser'
    },
    2: {
        'email': 'second@email.com',
        'name': 'Second User',
        'password': "secondpassword",
        'handle': "seconduser"
    }
}

handle = 'seconduser1'
flag = 0
for h in users.values():
    if h['handle'] == handle:
        print('handle exists')
        flag = 1
if not flag:
    print('handle does not exist')
    
