class Student ():
    def __init__(self, name, examGrades):
        self.name = name
        self.grades = examGrades
    
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student(name='Joko', examGrades=(95, 86, 77, 80, 85))
print(student.name)
print(student.average())
