from user import User

users = [
    User(1, 'joko', 'rahasia')
]

user_id_mapping = {
    user.id: user for user in users
}

user_name_mapping = {
    user.username: user for user in users
}


def authenticate(username, password):
    user = user_name_mapping.get(username, None)
    if user:
        if user.password == password:
            return user
    return None


def identity(payload):
    user_id = payload['identity']
    return user_id_mapping.get(user_id, None)
