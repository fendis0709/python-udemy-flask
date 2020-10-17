import os
import sqlite3


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def findByUsername(cls, username):
        connection = sqlite3.connect(os.path.relpath('data.db'))

        findUser = 'SELECT * FROM users WHERE username = ?'
        query    = connection.cursor().execute(findUser, (username,))
        result   = query.fetchone()

        user = None
        if result:
            user = cls(*result)
        
        connection.close()

        return user
    
    @classmethod
    def findById(cls, _id):
        connection = sqlite3.connect(os.path.relpath('data.db'))

        findUser = 'SELECT * FROM users WHERE id = ?'
        query    = connection.cursor().execute(findUser, (_id,))
        result   = query.fetchone()

        user = None
        if result:
            user = cls(*result)
        
        connection.close()

        return user
