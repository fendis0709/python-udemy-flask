import sqlite3
from flask import request
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.student import Student


class StudentResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This field is required'
                        )

    # Find student by ID
    def get(self, id):
        student = Student.find(id)
        if student is None:
            return {
                'message': 'Student not found'
            }, 404

        return {
            'student': student._json()
        }, 200

    # Update student by ID
    @jwt_required()
    def put(self, id):
        data = StudentResource.parser.parse_args()

        student = Student.find(id)
        if student is None:
            return {
                'message': 'Student not found'
            }, 400

        student = Student(_id=id, name=data['name'])
        student.update(id)

        return {
            'message': 'Student successfully updated'
        }, 200

    # Delete student by ID
    @jwt_required()
    def delete(self, id):
        Student.delete(id)

        return {
            'message': 'Student successfully deleted'
        }


class StudentsResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This field is required'
                        )

    # Get all students
    def get(self):
        rows = Student.get()

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
        data = StudentsResource.parser.parse_args()

        student = Student(_id=None, name=data['name'])
        student.insert()

        return {
            'message': 'Student created successfully'
        }, 201
