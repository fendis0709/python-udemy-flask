user = {'name': 'Joko', 'level': 'user'}
# user = {'name': 'Joko', 'level': 'admin'}


def secureAdminPassword(func):
    def secure():
        if(user['level'] == 'admin'):
            return func()
    return secure


def getAdminPassword():
    return '12345'


getAdminPassword = secureAdminPassword(getAdminPassword)
print(getAdminPassword())
