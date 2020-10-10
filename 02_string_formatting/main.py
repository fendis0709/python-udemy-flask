# String Formatting
name = 'Agus'
print(name)

# Implement F-String
print(f'Halo, {name}')

name = 'Roni'
print(f'Halo, {name}')

# Implement Format
name = 'Wahyu'
greeting = 'Halo, {}'
greetingWithName = greeting.format(name)
print(greetingWithName)

greetingWithName = greeting.format('Joko')
print(greetingWithName)

greetingToday = 'Halo, {}. Sekarang hari {}'
print(greetingToday.format('Andi', 'Senin'))
