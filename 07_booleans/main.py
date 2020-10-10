# Comparisons : '==', '!=', '>', '>=', '<', '<='
print(10 == 10)
print(10 != 10)
print(10 > 10)
print(10 >= 10)
print(10 < 10)
print(10 <= 10)

# Beware of using "is"
# "is" could be use to define the variable has the same value (value thaht print out, data type, and memory allocation)
friends = ['Joko', 'Andi']
family = ['Joko', 'Andi']
roommates = friends

print('Comparison "IS"')
print(friends == family)        # Will return 'True'
print(friends is family)        # Will return 'False' (Because it has different memory allocation, despite it has same value)
print(friends is roommates)     # Will return 'True' (Because variable 'roommates' using the same value & memory allocation as variable 'friends')