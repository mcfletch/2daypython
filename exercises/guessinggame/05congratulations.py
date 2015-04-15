import random
number = random.randint( 1, 100 )

success = False # we haven't yet succeeded
while not success:
    
    guess = raw_input('What is your guess? ')
    guess = int(guess) # guess was a string, now an integer
    
    if guess > number:
        print( "Too high")
    elif guess < number:
        print( "Too low")
    else:
        print( "You rock!" )
    
    success = (guess == number)
