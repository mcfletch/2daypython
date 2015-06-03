from __future__ import print_function
import random, time
random.seed(time.time())

import os
HERE = os.path.dirname(__file__)
DEFAULT_QUESTIONS = os.path.join(HERE, 'questions.csv')

def load_questions(filename=DEFAULT_QUESTIONS):
    """Load our questions from the filename
    
    Format of the file:
    
        question|answer|bad_answer|bad_answer...
    
    returns [
        [ 'question', 'answer', 'bad_answer',... ],
        [ 'question', 'answer', 'bad_answer',... ],
        ...
    ]
    """
    import csv
    questions = []
    for record in csv.reader(open(filename), delimiter='|'):
        if len(record) > 2: # skip empty lines
            questions.append(record)
    return questions

def reward( level_number ):
    """Reward should double for each level starting at 1000"""
    return 2**level_number * 1000

def display_status( level_number,  score, errors ):
    """Print out status report for a given level and current winnnings
    
    Uses string formatting to produce a nicely-formatted display
    """
    print("Level {0} for {1}pts    Score: {2}pts Errors: {3}/3".format(
        level_number+1, # note: normal people think in 1-index
        reward(level_number), # calculate it
        score, # current value we are tracking
        errors,
    ))

def display_questions( question,answers ):
    """Display the question and the answers
    
    * displays the answers with 1-indexed labels
    
    return None
    """
    print(question)
    for i,answer in enumerate(answers):
        print('    {0}) {1}'.format(i+1, answers[i]))

def get_response():
    """Ask the user to make a choice
    
    returns 0-indexed result or None if the user enters nothing
    """
    while True:
        try:
            content = raw_input("Your answer (Enter to Cancel)? ")
            if not content:
                return None
            return int(content) - 1
        except ValueError:
            print("Didn't recognize a number in that: {0!r}".format(content))
            pass 

def run_level( level_number, level, errors, score ):
    """Run a single level until user gets it correct, fails, or quits
    
    returns errors,score 
    raises SystemExit if the user fails or 
    """
    question,correct,answers = level[0],level[1],level[1:]
    random.shuffle(answers)
    
    correct_answer = False
    while not correct_answer:
        display_status(level_number, score, errors)
        display_questions( question,answers )
        response = get_response( )
        if response is None:
            # User has chosen to leave with current score
            print("Sorry to see you go!")
            return -1,score
        chosen = answers[response]
        if chosen == correct:
            print("Correct!\n")
            score += reward(level_number)
            correct_answer = True
        else:
            errors += 1
            score = score//2
            if errors >= 3:
                print("WRONG! Sorry, you've lost everything\n")
                score = 0
                break
            else:
                print("WRONG! %s Errors\n"%(errors,))
    return errors,score

def run_game():
    """Run the Trivia Game until the user exits, wins or loses"""
    errors = 0
    score = 0
    list_of_questions = load_questions()
    for level_number,level in enumerate(list_of_questions):
        errors,score = run_level( level_number, level, errors, score )
        if errors >= 3 or errors < 0:
            break
    if score:
        print("Your score was {:,}".format(score, ))
    else:
        print("Please try again!")
    raw_input("Press <enter> to leave > ")

#mainline_start
if __name__ == "__main__":
    run_game()
#mainline_stop
