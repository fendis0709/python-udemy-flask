from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Student(Resource):
    def get(self, slug):
        return {
            'name': 'Joko',
            'slug': slug
        }


api.add_resource(Student, '/students/<string:slug>')


app.run()
