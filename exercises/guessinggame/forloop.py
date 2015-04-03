answer = 64

for i in range(10):
    guess = raw_input('Guess the number (try %s/10)? '%(i, ))
    guess = int(guess)
    
    if guess == answer:
        print( "Right on!")
        break # stop the for loop
    elif i < 9:
        print( "Oops, try again." )
    else:
        print( "Sorry, not your day." )
