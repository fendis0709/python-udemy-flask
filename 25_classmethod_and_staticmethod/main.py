class Person:
    MARRIAGES = ('Married', 'Not Married')

    def __init__(self, name, age, married):
        self.name = name
        self.age = age
        self.married = married

    def __repr__(self):
        return f'<Class Person({self.name}, {self.age} years old. {self.married})>'

    @classmethod
    def married(cls, name, age):
        return cls(name, age, married=cls.MARRIAGES[0])

    @staticmethod
    def occupation(occupation):
        return f'<Class Person({occupation})>'


person = Person('Joko', 29, 'Married')
print(person.__repr__())
print(Person.married('Andi', 35))
print(Person.occupation('Farmer'))
