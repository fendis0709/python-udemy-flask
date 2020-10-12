# Declaring tuple doesn't need to add '()'
grades = 75, 85
print(grades[0])

# Assigning tuple dynamically
jokoGrade, roniGrade = 95, 85
print(jokoGrade)

# Deconstructing dictionary into tuple
studentAttendances = {'Joko': 95, 'Agus': 85, 'Wahyu': 100}
for attendance in studentAttendances.items() :
    # Notice that the result is a tuple
    print(attendance)

# Access value inside each tuple from list
friendAges = [('Joko', 25), ('Roni', 35)]
for name, age in friendAges :
    print(f'{name} is {age} years old')

# Collecting data (using asterisk symbol)
head, *tail = ['Joko', 'Andi', 'Agus']
print(head)
print(tail)

