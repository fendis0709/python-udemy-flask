# Define arguments inside function
def add(*numbers) :
    total = 0
    for number in numbers :
        total += number
    return total

print(add(1, 2, 3, 4, 5))

# Unpacking variable
def division(divisor, dividend) :
    return divisor / dividend

numbers = [1, 5]
print(division(*numbers))

# Magic unpacking variable
def multiply(x, y) :
    return x * y

numbers = {'x': 15, 'y': 65}
print(multiply(**numbers))

# Simple calculator using arguments
def calculator(*numbers, operation) :
    if operation == '+' :
        # Since the 'numbers' is a tupple
        # Don't forget to unpack tuple into variables
        # So the function read parameter as multiple variable, not single tuple
        return add(*numbers)
    else :
        return 'No operation found'

# Since it has arguments, parameter 'operation' must defined
print(calculator(1, 2, 3, 4, 5, operation='+'))