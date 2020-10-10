price = input('Input book price (in Rupiah): ')
discount = input('Input discount (in decimal): ')
result = int(price) * (1 - float(discount))
print(f'The book price now is {result:.2f} Rupiah')