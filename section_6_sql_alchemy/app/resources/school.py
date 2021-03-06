from flask_restful import Resource, reqparse
from models.school import School


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

    def delete(self, id):
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
    def get(self):
        schools = School.all()
        return {
            'code': 200,
            'schools': [school._json() for school in schools]
        }, 200

    # Mendaftarkan data sekolah
    def post(self):
        _input = SchoolsResource.parser.parse_args()

        school = School(id=None, name=_input['name'])
        school.save()

        return {
            'code': 201,
            'message': 'School data created successfully'
        }, 201
