import sqlite3


class User:
    def __init__(self, _id, name, email, password):
        self.id = _id
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def findByEmail(cls, email):
        connection = sqlite3.connect('data.db')

        query = 'SELECT * FROM users WHERE email = ?'
        result = connection.cursor().execute(query, (email,))
        result = result.fetchone()

        user = None
        if result:
            user = cls(*result)

        connection.close()

        return user

    @classmethod
    def findById(cls, _id):
        connection = sqlite3.connect('data.db')

        query = 'SELECT * FROM users WHERE id = ?'
        result = connection.cursor().execute(query, (_id,))
        result = result.fetchone()

        user = None
        if result:
            user = cls(*result)

        connection.close()

        return user
