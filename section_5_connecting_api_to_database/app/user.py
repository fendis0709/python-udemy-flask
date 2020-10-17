from flask_restful import Resource, reqparse, request
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


class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type=str,
        required=True,
        help='This field is required'
    )
    parser.add_argument('password', 
        type=str,
        required=True,
        help='This field is required'
    )

    def post(self):
        _input = UserResource.parser.parse_args()

        user = User.findByUsername(_input['username'])
        if user :
            return {
                'message': f"A user with username '{_input['username']}' already exists"
            }, 400

        connection = sqlite3.connect('data.db')

        insert  = "INSERT INTO users VALUES (NULL, ?, ?)"
        data    = (_input['username'], _input['password'])
        connection.cursor().execute(insert, data)

        connection.commit()

        connection.close()

        return {
            'message': 'User successfully created'
        }, 201
