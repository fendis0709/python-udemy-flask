from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

students = [
    {
        'id': 1,
        'name': 'Joko',
        'grades': [
            {
                'name': 'mathematic',
                'score': 90
            },
            {
                'name': 'science',
                'score': 95
            }
        ]
    }
]


@app.route('/')
def main():
    return 'Hello, world!'


# Get students list
# GET   : {host}/students
@app.route('/students')
def getStudent():
    # return 'student-list'
    return jsonify({
        'students': students
    })


# Get student detail
# GET : {host}/students/<int:id>
@app.route('/students/<int:id>')
def getStudentDetail(id):
    # return f'student-detail:{id}'
    detail = None
    for student in students:
        if id == student['id']:
            detail = student
    return jsonify({
        'student': detail
    })


# Register new student
# POST : {host}/students
@app.route('/students', methods=['POST'])
def registerStudent():
    # return 'student-register'
    student = request.json
    student['id'] = len(students) + 1
    students.append(student)
    return jsonify({
        'students': students
    })


# Update student
# PUT : {host}/students/<int:id>
@app.route('/students/<int:id>', methods=['PUT'])
def updateStudent(id):
    return f'student-update:{id}'


# Delete student
# DELETE : {host}/students/<int:id>
@app.route('/students/<int:id>', methods=['DELETE'])
def deleteStudent(id):
    return f'student-delete:{id}'


app.run(port=5000)
