import random
number = random.randint( 1, 100 )

guess = 0
while guess != number:

    guess = raw_input('What is your guess? ')
    guess = int(guess)

    if guess == number:
        print( "Yay!")
    elif guess > number:
        print( "Too high")
    else:
        print( "Too low")

