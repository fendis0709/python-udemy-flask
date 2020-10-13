class Classroom:
    def __init__(self, *students):
        self.students = students

    def __str__(self):
        return f'This classroom already has {len(self.students)} students.'


class Student(Classroom):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Student Name : {self.name}'


student1 = Student('Joko')
student2 = Student('Roni')
classroom = Classroom(student1, student2)

print(student1)
print(student2)
print(classroom)
