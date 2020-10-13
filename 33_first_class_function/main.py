def multiply(self, *numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


def operation(*numbers, operator):
    return operator(*numbers)


print(multiply(1, 2, 3, 4, 5))
print(operation(1, 2, 3, 4, 5, operator=multiply))
