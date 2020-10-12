def divide(dividend, divisor):
    if divisor != 0 :
        result = dividend/divisor
        print(f'Result: {result:.2f}')
    else :
        print('Dividing by zero is not allowed')

print('Welcome. Let\'s calculate division.')
dividend    = input('Please input dividend number : ')
divisor     = input('Please input divisor number : ')

# Call function
divide(int(dividend), int(divisor))

# Call function using naming argument
divide(dividend=int(dividend), divisor=int(divisor))