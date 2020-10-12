def amongUs():
    crewmates   = ('Green', 'Brown', 'Black', 'White', 'Red')
    impostor    = 'Red'
    print(crewmates)
    print('There\'s one impostor among us.')
    guess   = input('Who\'s the impostor? ')
    if(guess.lower() == impostor):
        print('Congratulation. You answer correctly!')
    else :
        print('Sorry, wrong answer')

amongUs()
