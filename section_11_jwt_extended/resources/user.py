from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    fresh_jwt_required,
    get_jwt_claims,
    get_jwt_identity,
    jwt_refresh_token_required,
)
from flask_restful import Resource, reqparse, request
from models.user import UserModel as User


class UserResource(Resource):
    # Menampilkan data akun pengguna berdasarkan id
    def get(self, id):
        user = User.find(id)
        if user is None:
            return {
                'message': 'User not found'
            }, 404

        return {
            'code': 200,
            'user': user._json()
        }, 200

    # Menghapus data akun pengguna
    def delete(self, id):
        claims = get_jwt_claims()
        if claims['is_admin'] is None:
            return {
                'code': 403,
                'message': 'You shall not pass!'
            }, 403

        user = User.find(id)
        if user is None:
            return {
                'code': 403,
                'message': 'User not found'
            }, 400

        user.delete()

        return {
            'code': 200,
            'message': 'User deleted successfully'
        }, 200


class UsersResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help='This field is required'
    )
    parser.add_argument(
        'email',
        type=str,
        required=True,
        help='This field is required'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field is required'
    )

    # Mendaftarkan akun pengguna baru
    def post(self):
        _input = self.parser.parse_args()

        user = User.find_by_email(_input['email'])
        if user:
            return {
                'message': f"A user with email '{_input['email']}' already exists"
            }, 400

        user = User(
            _id=None,
            name=_input['name'],
            email=_input['email'],
            password=_input['password']
        )
        user.save()

        return {
            'code': 201,
            'message': 'User created successfully'
        }, 201


class UserAuth(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        required=True,
        help='This field is required'
    )
    parser.add_argument(
        'password',
        required=True,
        help='This field is required'
    )

    @classmethod
    def post(cls):
        _input = cls.parser.parse_args()

        user = User.find_by_email(_input['email'])
        if user is None:
            return {
                'message': 'Credential not match'
            }, 401

        if user.password != _input['password']:
            return {
                'message': 'Credential not match'
            }, 401

        access_token = create_access_token(identity=user.id, fresh=True)
        refrech_token = create_refresh_token(identity=user.id)

        return {
            'user': {
                'id': user.id,
                'name': user.name
            },
            'access_token': access_token,
            'refresh_token': refrech_token
        }, 200


class RefreshToken(Resource):
    # Generate new access token
    @jwt_refresh_token_required
    def get(self):
        user_id = get_jwt_identity()
        user = User.find(user_id)
        access_token = create_access_token(identity=user_id, fresh=False)
        return {
            'user': {
                'id': user.id,
                'name': user.name
            },
            'access_token': access_token,
            'refresh_token': None
        }
