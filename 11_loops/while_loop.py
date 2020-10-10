magicNumbers = {1, 5, 9}

confirm = input('Wanna play Bingo? (Y/n) ')

while confirm.lower() == 'y' :
    guessNumber = input('Guess our number : ')
    if int(guessNumber) in magicNumbers :
        print('You\'re answer correctly. Lucky one.')
    else :
        print('Sorry wrong answer')
    
    confirm = input('Wanna play again? (Y/n) ')
    