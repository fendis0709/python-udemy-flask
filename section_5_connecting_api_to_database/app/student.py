import sqlite3
from flask import request
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse


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

        if result:
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
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This field is required'
                        )

    # Get all students
    def get(self):
        connection = sqlite3.connect('data.db')

        query   = 'SELECT * FROM students ORDER BY name'
        result  = connection.cursor().execute(query)
        rows    = result.fetchmany()

        connection.close()

        students = []
        if rows:
            for row in rows:
                students.append({
                    'id': row[0],
                    'name': row[1]
                })

        return {
            'message': f'There are {len(students)} student(s) found',
            'students': students
        }, 200

    # Register new student
    @jwt_required()
    def post(self):
        _input = Students.parser.parse_args()

        connection = sqlite3.connect('data.db')

        insert = 'INSERT INTO students VALUES (NULL, ?)'
        connection.cursor().execute(insert, (_input['name'],))

        connection.commit()

        connection.close()

        return {
            'message': 'Student created successfully'
        }, 201
