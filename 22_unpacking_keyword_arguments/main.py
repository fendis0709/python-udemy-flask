# Defining keyword argument inside function
def person(**data) :
    return data

print(person(name='Joko', age=26))

# Defining keyword argument inside function and callable
personData = {'name': 'Roni', 'age': 19}
print(person(**personData))

# Usage example of argument (args) and named argument (kwargs / keyword arguments)
def sayAnithing(*args, **kwargs) :
    print(args)
    print(kwargs)

sayAnithing(1, 2, 3, name='Doni', age=15)