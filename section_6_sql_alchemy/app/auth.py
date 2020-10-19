from resources.user import User


def authenticate(email, password):
    user = User.findByEmail(email)
    if user:
        if user.password == password:
            return user
    return None


def identity(payload):
    userId = payload['identity']
    return User.findById(userId)
