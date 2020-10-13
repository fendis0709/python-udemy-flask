from typing import List


class Student:
    # ----- Avoid this code (List are mutable value)
    # def __init__(self, name: str, grades: List[int] = []):
    # ----- Use this approach
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []

    def takeExam(self, score: int):
        self.grades.append(score)


joko = Student('Joko')
joko.takeExam(90)
print(joko.grades)

roni = Student('Roni')
print(roni.grades)
