from database import db
from datetime import timedelta
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resources.user import UserResource as User, UsersResource as Users, UserAuth, RefreshToken
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

# Append new data to JWT


@jwt.user_claims_loader
def add_jwt_claim(identity):
    if identity == 1:
        return {
            'is_admin': True
        }
    return {
        'is_admin': False
    }

# Handler token JWT expired


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'code': 401,
        'message': 'Token has been expired'
    }), 401

# Invalid token JWT


@jwt.invalid_token_loader
def invalid_token_callback():
    return jsonify({
        'code': 401,
        'message': 'Token invalid'
    }), 401

# No token JWT provided from user


@jwt.unauthorized_loader
def not_provided_token_callback():
    return jsonify({
        'code': 401,
        'message': 'Token required'
    }), 401


@jwt.needs_fresh_token_loader
def require_fresh_token_callback():
    return jsonify({
        'code': 401,
        'message': 'Fresh token requires'
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'code': 401,
        'message': 'Token is expired'
    }), 401


api = Api(app)
api.add_resource(UserAuth, '/login')
api.add_resource(RefreshToken, '/refresh-token')
api.add_resource(Students, '/students')
api.add_resource(Student, '/students/<int:id>')
api.add_resource(Schools, '/schools')
api.add_resource(School, '/schools/<int:id>')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')

db.init_app(app)

app.run(debug=True)
