import functools

user = {'name': 'Joko', 'level': 'user'}
user = {'name': 'Joko', 'level': 'admin'}


def secureAdminPassword(func):
    # Remember always using this function tools when using function decorator
    @functools.wraps(func)
    def secure():
        if(user['level'] == 'admin'):
            return func()
    return secure


# @<name_of_method_decorator>
@secureAdminPassword
def getAdminPassword():
    return '12345'


getAdminPassword = secureAdminPassword(getAdminPassword)
print(getAdminPassword.__name__)
print(getAdminPassword())
