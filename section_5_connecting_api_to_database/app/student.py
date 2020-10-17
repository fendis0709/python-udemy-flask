import sqlite3
from flask import request
from flask_jwt import jwt_required
from flask_restful import Resource


students = [
    {
        'id': 1,
        'name': 'Joko',
    }
]

class Student(Resource):
    # Find student by ID
    def get(self, id):
        connection = sqlite3.connect('data.db')

        querySearch = 'SELECT * FROM students WHERE id = ?'
        queryResult = connection.cursor().execute(querySearch, (id,))

        result = queryResult.fetchone()

        connection.close()

        if result :
            return {
                'student': result
            }, 200

        return {
            'message': 'No student found'
        }, 404

    # Update student by ID
    @jwt_required()
    def put(self, id):
        data = request.get_json()
        student = next(
            filter(lambda student: student['id'] == id, students), None)
        if student:
            student.update({
                'id': student['id'],
                'name': data['name']
            })
        return {
            'student': student
        }

    # Delete student by ID
    @jwt_required()
    def delete(self, id):
        global students  # Use global to avoid re-assignment error
        students = list(filter(lambda student: student['id'] != id, students))
        return {
            'students': students
        }


class Students(Resource):
    # Get all students
    def get(self):
        return {
            'students': students
        }, 200

    # Register new student
    @jwt_required()
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
