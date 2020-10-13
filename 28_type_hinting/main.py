class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age} years old.'

    def isMarried(self, gender: str) -> str:
        if(gender.lower() == 'male'):
            if(self.age >= 25):
                return 'Married'
            return 'Not Married'
        elif (gende.lower() == 'female'):
            if (self.age >= 19):
                return 'Married'
            return 'Not Married'


person = Person('Joko', 27)
print(person)
print(person.isMarried('male'))
