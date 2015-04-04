# from 1 to 100
import random
number = random.randint( 1, 100)

possible = range(1, 101)
# user has to guess, how do we get their guess?
while True:
    print( 'Numbers Left: %s'%(" ".join([str(x) for x in possible])))
    guess = raw_input("What's your guess?")
    guess = int(guess)
    print('You guessed: %r'% guess)
    if guess == number:
        print( "Yay, you rock!" )
        break
    elif guess > number:
        print( "Too high" )
        possible = [p for p in possible if p < guess]
    else:
        print( "Too low" )
        possible = [p for p in possible if p > guess]
