#! /usr/bin/env python

# we want to use a pre-built library of functions called "random"
import random
# we want to get a random integer between 0 and 100
answer = random.randint(0, 100)

for i in range(10):
    guess = raw_input('Guess the number (try %s/10)? '%(i+1, ))
    guess = int(guess)
    if guess == answer:
        print( "Right on!")
        break
    elif i < 9:
        if guess > answer:
            print ('Too high.')
        else:
            print ('Too low.')
    else:
        print( "Sorry, not your day." )
