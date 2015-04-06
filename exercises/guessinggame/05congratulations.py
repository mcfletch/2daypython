import random
number = random.randint( 1, 100 )

guess = 0
while not (guess == number):

    guess = raw_input('What is your guess? ')
    guess = int(guess)

    if guess > number:
        print( "Too high")
    elif guess < number:
        print( "Too low")

print( "You rock!" )
