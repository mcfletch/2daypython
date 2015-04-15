import random
number = random.randint( 1, 100 )

success = False
while not success:

    guess = raw_input('What is your guess? ')
    guess = int(guess)

    if guess > number:
        print( "Too high")
    elif guess < number:
        print( "Too low")

    success = (guess == number)
