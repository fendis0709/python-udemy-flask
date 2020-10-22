from flask_restful import Resource, reqparse, request
from models.user import UserModel as User


class UserResource(Resource):
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
        _input = UserResource.parser.parse_args()

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
            'message': 'User successfully created'
        }, 201
