answer = 64

while True:
    guess = raw_input('Guess the number? ')
    guess = int(guess)
    
    if guess == answer:
        print( "Right on!")
        break # stop the while loop
    else:
        print( "Oops, try again.")
