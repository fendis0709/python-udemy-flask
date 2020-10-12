def dayOfAge(age = 0) :
    if age >= 0 :
        result = age * 365
        return result
    else :
        return 0

print('Let\'s calculate dayof your age')
age     = input('Enter your age : ')
days    = dayOfAge(age=int(age))
print(f'You\'ve been passed {days} days from your birthdate')