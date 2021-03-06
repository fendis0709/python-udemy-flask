from flask import request
from flask_jwt_extended import jwt_required, jwt_optional, get_jwt_claims, get_jwt_identity, fresh_jwt_required
from flask_restful import Resource, reqparse
from models.student import StudentModel as Student


class StudentResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help='This field is required'
    )
    parser.add_argument(
        'school_id',
        type=int,
        required=True,
        help='This field is required'
    )

    # Find student by ID
    def get(self, id):
        student = Student.find(id)
        if student is None:
            return {
                'code': 404,
                'message': 'Student data not found'
            }, 404

        return {
            'code': 200,
            'student': student._json()
        }, 200

    # Update student by ID
    @jwt_required
    def put(self, id):
        data = StudentResource.parser.parse_args()

        student = Student.find(id)
        if student is None:
            return {
                'code': 400,
                'message': 'Student data not found'
            }, 400

        student.name = data['name']
        student.school_id = data['school_id']
        student.save()

        return {
            'code': 200,
            'message': 'Student data successfully updated'
        }, 200

    # Delete student by ID
    @fresh_jwt_required
    def delete(self, id):
        student = Student.find(id)
        if student is None:
            return {
                'code': 400,
                'message': 'School data not found'
            }, 400

        Student.delete(id)
        return {
            'code': 200,
            'message': 'Student data successfully deleted'
        }, 200


class StudentsResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help='This field is required'
    )
    parser.add_argument(
        'school_id',
        type=int,
        required=True,
        help='This field is required'
    )

    # Get all students
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity()
        if user_id is None:
            return {
                'code': 200,
                'students': []
            }, 200

        students = Student.get()
        return {
            'code': 200,
            'students': list(student._json() for student in students)
        }, 200

    # Register new student
    @jwt_required
    def post(self):
        data = StudentsResource.parser.parse_args()

        student = Student(
            _id=None,
            name=data['name'],
            school_id=data['school_id']
        )
        student.save()

        return {
            'code': 201,
            'message': 'Student data created successfully'
        }, 201
