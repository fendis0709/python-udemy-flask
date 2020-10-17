from auth import authenticate, identity
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from user import UserResource
from student import Student, Students


app = Flask(__name__)
app.secret_key = 'helloworld'
api = Api(app)

JWT(app=app, authentication_handler=authenticate, identity_handler=identity)

api.add_resource(Students, '/students')
api.add_resource(Student, '/students/<int:id>')
api.add_resource(UserResource, '/users')

app.run()
