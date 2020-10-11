# 1. Using simple calculation on List
grades = [75, 85, 90, 80]
print(grades)

# 1.a. Conventional approach (Using for-loops)
gradesMultiple = []
for grade in grades :
    gradesMultiple.append(grade * 2)
print(gradesMultiple)

# 1.b. Advance list
gradesMultiple = [grade * 2 for grade in grades]
print(gradesMultiple)

# 2. Using simple if-statement
friends = ['Andi', 'Joko', 'Agus', 'Roni']
print(friends)

# 2.a. Conventional approach (Using for-loops)
friendsStartWithA = []
for friend in friends :
    if friend.startswith('A') :
        friendsStartWithA.append(friend)
print(friendsStartWithA)

# 3.b Advance list
friendsStartWithA = [friend for friend in friends if friend.startswith('A')]
print(friendsStartWithA)