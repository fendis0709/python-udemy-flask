from auth import authenticate, identity
from database import db
from datetime import timedelta
from flask import Flask, jsonify
from flask_jwt import JWT
from flask_restful import Api
from resources.user import UserResource
from resources.student import StudentResource, StudentsResource
from resources.school import SchoolResource, SchoolsResource


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
api.add_resource(StudentsResource, '/students')
api.add_resource(StudentResource, '/students/<int:id>')
api.add_resource(SchoolsResource, '/schools')
api.add_resource(SchoolResource, '/schools/<int:id>')
api.add_resource(UserResource, '/users')

db.init_app(app)

app.run()
