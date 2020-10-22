from auth import authenticate, identity
from database import db
from datetime import timedelta
from flask import Flask, jsonify
from flask_jwt import JWT
from flask_restful import Api
from resources.user import UserResource as User, UsersResource as Users
from resources.student import StudentResource as Student, StudentsResource as Students
from resources.school import SchoolResource as School, SchoolsResource as Schools


app = Flask(__name__)
app.secret_key = 'helloworld'

app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWT(
    app=app,
    authentication_handler=authenticate,
    identity_handler=identity
)


@jwt.auth_response_handler
def customResponse(access_token, identity):
    return jsonify({
        'token': access_token.decode('utf-8'),
        'user': {
            'id': identity.id,
            'name': identity.name
        }
    })


@jwt.jwt_error_handler
def custom_error_handler(error):
    return jsonify({
        'code': error.status_code,
        'message': error.description
    }), error.status_code


api = Api(app)
api.add_resource(Students, '/students')
api.add_resource(Student, '/students/<int:id>')
api.add_resource(Schools, '/schools')
api.add_resource(School, '/schools/<int:id>')
api.add_resource(User, '/users')
api.add_resource(Users, '/users/<int:id>')

db.init_app(app)

app.run(debug=True)
