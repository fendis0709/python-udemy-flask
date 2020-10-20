from models.user import User


def authenticate(email, password):
    user = User.find_by_email(email)
    if user:
        if user.password == password:
            return user
    return None


def identity(payload):
    userId = payload['identity']
    return User.find(userId)
