# We want the user to guess this value...
answer = "64"

# We ask the user to make the guess
guess = raw_input('Guess the number? ')

if guess == answer:
    print( "Right on!")
else:
    print( "Oops, try again.")
