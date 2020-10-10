# List (array)
# - Always print in order (0, 1, 2, ...)
# - Can be accessed using key index
# - Can store duplicate value
# - Can be modified (add, remove, update value of element)
listName = ['Joko', 'Andi', 'Roni']

# Tuple
# - Always print in order (0, 1, 2, ...)
# - Can be accessed using key index
# - Can store duplicate value
# - Can't be modified (add, remove, update value of element)
tupleName = ('Joko', 'Andi', 'Roni')

# Set
# - Don't alwys print in order (0, 2, 1, ...)
# - Can't be accessed using key index
# - Can't store duplicate value
# - Can be modified (add, remove, update value of element)
setName = {'Joko', 'Andi', 'Roni'}

# ----- List -----
print('----- LIST -----')

# Always print in order
print(listName)

# Can be accessed using key index
print(listName[0])

# Can add, remove, update value of element
listName[0] = 'Agus'
listName.append('Zainal')
listName.remove('Andi')
print(listName)

# ----- Tuple -----
print('----- TUPLE -----')

# Always print in order
print(tupleName)

# Can be accessed using key index
print(tupleName[0])

# ----- Set -----
print('----- Set -----')

# Don't always print in order
print(setName)

# Can add, remove, update value of element
setName.add('Rizky')
print(setName)

# Don't allow duplicate value
setName.add('Andi')
print(setName)
