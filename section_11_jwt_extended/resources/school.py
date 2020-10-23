from flask_jwt_extended import jwt_required, jwt_optional, get_jwt_claims, get_jwt_identity
from flask_restful import Resource, reqparse
from models.school import SchoolModel as School


class SchoolResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help='This field is required'
    )

    # Menampilkan data sekolah berdasarkan id
    def get(self, id):
        school = School.find(id)
        if school is None:
            return {
                'code': 404,
                'message': 'School data not found'
            }, 404

        return {
            'code': 200,
            'school': school._json()
        }, 200

    # Memperbarui data sekolah berdasarkan id
    @jwt_required
    def put(self, id):
        _input = SchoolResource.parser.parse_args()

        school = School.find(id)
        if school is None:
            return {
                'code': 400,
                'message': 'School data not found'
            }, 400

        school.name = _input['name']
        school.save()

        return {
            'code': 200,
            'message': 'School data updated successfully'
        }, 200

    # Menghapus data sekolah berdasarkan id
    @jwt_required
    def delete(self, id):
        claims = get_jwt_claims()
        if claims['is_admin'] is not True :
            return {
                'code': 403,
                'message': 'You shall not pass!'
            }, 403

        school = School.find(id)
        if school is None:
            return {
                'code': 400,
                'message': 'School data not found'
            }, 400

        school.delete()

        return {
            'code': 200,
            'message': 'School data deleted successfully'
        }, 200


class SchoolsResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help='This field is required'
    )

    # Menampilkan semua data sekolah
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity()
        if user_id is None :
            return {
                'code': 200,
                'schools': []
            }, 200

        schools = School.all()
        return {
            'code': 200,
            'schools': [school._json() for school in schools]
        }, 200

    # Mendaftarkan data sekolah
    @jwt_required
    def post(self):
        _input = SchoolsResource.parser.parse_args()

        school = School(id=None, name=_input['name'])
        school.save()

        return {
            'code': 201,
            'message': 'School data created successfully'
        }, 201
