# Defining lambda function with name
add = lambda a, b: a + b
print(add(1, 2))

# Defining lambda directly
print((lambda a, b: a + b)(5, 6))

# Defining lambda using list
numbers = [2, 4, 6, 8]
print([(lambda number: number * number)(number) for number in numbers])
print(list(map((lambda number: number * number), numbers)))