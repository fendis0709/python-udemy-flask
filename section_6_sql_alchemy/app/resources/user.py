import os
import sqlite3
from flask_restful import Resource, reqparse, request
from models.user import User


class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This field is required'
                        )
    parser.add_argument('email',
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

        user = User.findByEmail(_input['email'])
        if user:
            return {
                'message': f"A user with email '{_input['email']}' already exists"
            }, 400

        connection = sqlite3.connect('data.db')

        insert = "INSERT INTO users VALUES (NULL, ?, ?, ?)"
        data = (_input['name'], _input['email'], _input['password'])
        connection.cursor().execute(insert, data)

        connection.commit()

        connection.close()

        return {
            'message': 'User successfully created'
        }, 201
