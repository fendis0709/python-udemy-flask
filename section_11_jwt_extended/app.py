from database import db
from datetime import timedelta
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resources.user import UserResource as User, UsersResource as Users, UserAuth
from resources.student import StudentResource as Student, StudentsResource as Students
from resources.school import SchoolResource as School, SchoolsResource as Schools


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'helloworld'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = app.config['JWT_SECRET_KEY']

jwt = JWTManager(app)

@app.route('/')
def hello():
    return 'Hello, World!'


api = Api(app)
api.add_resource(UserAuth, '/login')
api.add_resource(Students, '/students')
api.add_resource(Student, '/students/<int:id>')
api.add_resource(Schools, '/schools')
api.add_resource(School, '/schools/<int:id>')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')

db.init_app(app)

app.run(debug=True)
