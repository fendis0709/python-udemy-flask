# 1. Simple dictionary access
# Accessing dictionary using it's key (not index)
friendAges = {'Joko': 85, 'Roni': 75, 'Yoga': 95}
print(friendAges['Joko'])

# 2. Multiple dictionary access
# Accessing discionary inside list (using index of list)
friends = [
    {'name': 'Joko', 'age': 26},
    {'name': 'Roni', 'age': 25},
    {'name': 'Yoga', 'age': 28}
]
print(friends[2]['name'])

# 3. Accessing dictionary using for-loops
friendAttendances = {'Joko': 95, 'Roni': 85}

# 3.1. Dictionary only return it's key (index), not value
for friend in friendAttendances :
    print(friend)
    print(friendAttendances[friend])

# 3.2. To access using for-loops, use '.items()' method
for friend, attandance in friendAttendances.items() :
    print(f'{friend} has {attandance}% attendance')

# 3.2. To access it's value, use '.values()' method
friendAttendanceValues = friendAttendances.values()
averageAttendance = sum(friendAttendanceValues) / len(friendAttendanceValues)
print(f'This class has {averageAttendance}% attendance')