confirm = input('Wanna play a game (Y/N)? ')

impostor  = (1, 2)
impostors = {'Red', 'Green'}
crewmates = {'Yellow', 'Brown', 'Black'}
if confirm.lower() == 'y' :
    print('We have 5 players here.')
    print(crewmates.union(impostors))
    guessImpostor = input('How many impostor do you guess? ')
    if int(guessImpostor) in impostor :
        print('Nice answer. You guess the correct number.')
        whoImpostor = input('Now, who\'s the impostor? ')
        if(whoImpostor in impostors) :
            print('You answer correctly. Genius.')
        else :
            print('Sorry, wrong answer')
    else :
        print('Nope, there\'s two impostors among us')
