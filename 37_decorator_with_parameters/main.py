import functools


def securePassword(accessLevel):
    def decorator(func):
        # Remember always using this function tools when using function decorator
        @functools.wraps(func)
        def secure(*args, **kwargs):
            if(user['level'] == accessLevel):
                return func(*args, **kwargs)
            else:
                return f'No {accessLevel} access level for {user["name"]}'
        return secure
    return decorator


# @<name_of_method_decorator>(<parameter>)
@securePassword('admin')
def getAdminPassword():
    return 'admin: 09876'


# @<name_of_method_decorator>(<parameter>)
@securePassword('user')
def getUserPassword():
    return 'user: 12345'


user = {'name': 'Joko', 'level': 'user'}
print(user)
print(getAdminPassword())
print(getUserPassword())

user = {'name': 'Joko', 'level': 'admin'}
print(user)
print(getAdminPassword())
print(getUserPassword())
