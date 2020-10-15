from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

students = [
    {
        'id': 1,
        'name': 'Joko',
    }
]


class Student(Resource):
    # Find student by ID
    def get(self, id):
        for student in students:
            if student['id'] == id:
                return {
                    'student': student
                }, 200
        return {
            'student': None
        }, 404


class Students(Resource):
    # Get all students
    def get(self):
        return {
            'students': students
        }, 200

    # Register new student
    def post(self):
        data = request.get_json()
        counter = len(students)
        student = {
            'id': counter + 1,
            'name': data['name'],
        }
        students.append(student)
        return {
            'students': students
        }, 201


api.add_resource(Students, '/students')
api.add_resource(Student, '/students/<int:id>')


app.run()
