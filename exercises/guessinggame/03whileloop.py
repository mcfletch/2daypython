import random
number = random.randint( 1, 100 )

success = False
while not success:

    guess = raw_input('What is your guess? ')
    guess = int(guess)
    
    success = (guess == number)
