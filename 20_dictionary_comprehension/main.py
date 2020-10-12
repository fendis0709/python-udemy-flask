users = [
    (0, 'Joko', 'j0k0t0l3'),
    (1, 'Roni', 'rahasia'),
    (2, 'Wahyu', 'wahyu123')
]

usersMap = {user[1]: user for user in users}
print(usersMap)

usernameInput   = input('Enter your username: ')
passwordInput   = input('Enter your password: ')

_, username, password = usersMap[usernameInput]

if(password == passwordInput) :
    print('User found')
    print(usersMap[usernameInput])
else :
    print('Your credential is wrong')