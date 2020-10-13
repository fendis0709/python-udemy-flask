user = {'name': 'Joko', 'level': 'user'}
# user = {'name': 'Joko', 'level': 'admin'}


def getAdminPassword():
    return '12345'


def secureAdminPassword(func):
    def secure():
        if(user['level'] == 'admin'):
            return func()
    return secure


getAdminPassword = secureAdminPassword(getAdminPassword)
print(getAdminPassword())
