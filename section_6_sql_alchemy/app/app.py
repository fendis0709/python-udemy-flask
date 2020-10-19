from auth import authenticate, identity
from datetime import timedelta
from flask import Flask, jsonify
from flask_jwt import JWT
from flask_restful import Api
from resources.user import UserResource
from resources.student import StudentResource, StudentsResource


app = Flask(__name__)
app.secret_key = 'helloworld'

app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

jwt = JWT(app=app,
          authentication_handler=authenticate,
          identity_handler=identity)


@jwt.auth_response_handler
def customResponse(accessToken, identity):
    return jsonify({
        'token': accessToken.decode('utf-8'),
        'user': {
            'id': identity.id,
            'name': identity.name
        }
    })


api = Api(app)
api.add_resource(StudentsResource, '/students')
api.add_resource(StudentResource, '/students/<int:id>')
api.add_resource(UserResource, '/users')

app.run()
