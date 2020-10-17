from user import User


def authenticate(username, password):
    user = User.findByUsername(username)
    if user:
        if user.password == password:
            return user
    return None


def identity(payload):
    userId = payload['identity']
    return User.findById(userId)
