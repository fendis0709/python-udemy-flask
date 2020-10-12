class Person ():
    def __init__(self):
        self.name = 'Joko'
        self.age = 36

    # Use for convert object in class to string (If user only call class, not a method)
    def __str__(self):
        return f'My name is {self.name}. I\'m {self.age} years old.'

    # Use for convert object in class to string but only for Debugging
    # This method only works for Debugging
    # To test this method, you should call method directly as usual
    def __repr__(self):
        return f'<Object(\'{self.name}\', {self.age})>'


person = Person()
print(person)
print(person.__repr__())