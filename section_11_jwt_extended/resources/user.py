from flask_jwt_extended import create_access_token, create_refresh_token
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
            'user': user._json()
        }, 200

    # Menghapus data akun pengguna
    def delete(self, id):
        user = User.find(id)
        if user is None:
            return {
                'message': 'User not found'
            }, 400

        user.delete()

        return {
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
        }
