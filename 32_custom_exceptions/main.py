class TooManyStudentRegistered(ValueError):
    pass


class Classroom:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.remain = capacity
        self.occupied = 0

    def __repr__(self):
        return f'<{self.name}. Has {self.capacity} seat(s)>'

    def register(self, student: int):
        if(self.remain - student < 0):
            raise TooManyStudentRegistered(
                f'This classroom only has {self.remain} seat(s) remaining, but you register {student} student(s)'
            )
        self.occupied += student
        self.remain -= student


try:
    classroom = Classroom('Kelas XII - A', 50)
    print(classroom)

    classroom.register(1)
    print(f'The classroom now has {classroom.remain} seat(s)')

    classroom.register(55)
    print(f'The classroom now has {classroom.remain} seat(s)')
except TooManyStudentRegistered as exception:
    print(exception)
