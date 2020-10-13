import functools

user = {'name': 'Joko', 'level': 'user'}
user = {'name': 'Joko', 'level': 'admin'}


def secureAdminPassword(func):
    # Remember always using this function tools when using function decorator
    @functools.wraps(func)
    def secure(*args, **kwargs):
        if(user['level'] == 'admin'):
            return func(*args, **kwargs)
    return secure


# @<name_of_method_decorator>
@secureAdminPassword
def getPassword(panel):
    if panel == 'admin':
        return '12345'
    else:
        return 'No panel supplied'


print(getPassword.__name__)
print(getPassword('admin'))
