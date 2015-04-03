answer = 64
guess = raw_input('Guess the number? ')

# Convert the value to an integer
guess = int(guess)

if guess == answer:
    print( "Right on!")
else:
    print( "Oops, try again.")
