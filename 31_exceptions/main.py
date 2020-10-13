def division(dividend, divisor):
    if(divisor == 0):
        raise ZeroDivisionError('No zero divisor allowed')
    elif dividend < 0 or divisor < 0:
        raise ValueError('No negative value allowed')
    else:
        return dividend / divisor


students = [
    {'name': 'Joko', 'grades': [95, 85, 90]},
    {'name': 'Roni', 'grades': [-35, 0, -90]},
    {'name': 'Yoga', 'grades': []}
]

print('--- Welcome to average calculator program ---')
try:
    calculate = 0
    for student in students:
        total = sum(student['grades'])
        grades = len(student['grades'])
        average = division(total, grades)
        calculate += 1
        print(f"{student['name']} has average grade: {average:.2f}")
except ZeroDivisionError:
    calculate -= 1
    print('This student has no grades yet.')
except ValueError as exception:
    calculate -= 1
    print(exception)
finally:
    print(f'Successfully calculate {len(students)} students grades')
