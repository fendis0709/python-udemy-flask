import functools


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


user = {'name': 'Joko', 'level': 'user'}
print(getAdminPassword.__name__)
print(getAdminPassword())

user = {'name': 'Joko', 'level': 'admin'}
print(getAdminPassword.__name__)
print(getAdminPassword())
