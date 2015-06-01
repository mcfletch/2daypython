import random, time
random.seed(time.time())

#read_file_start
import os
HERE = os.path.dirname(__file__)
DEFAULT_QUESTIONS = os.path.join(HERE, 'questions.txt')

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
    questions = []
    for line in open(filename):
        questions.append(read_line(line))
    return questions

def read_line(line):
    """Process a single line from the questions
    
    * strip off the newline character
    * split the line on '|' characters
    
    returns list of fields
    """
    line = line.strip()
    line = line.split('|')
    return line
#read_file_stop

def reward( level_number ):
    """Reward should double for each level starting at $1000"""
    return 2**level_number * 1000

def display_status( level_number,  winnings ):
    """Print out status report for a given level and current winnnings
    
    Uses string formatting to produce a nicely-formatted display
    """
    print "Level {} for ${}    Current winnings: ${:,}".format(
        level_number+1, # note: normal people think in 1-index
        reward(level_number), # calculate it
        winnings, # current value we are tracking
    )

def display_questions( question,answers ):
    """Display the question and the shuffled answers
    
    * shuffles the answers randomly
    * displays the answers with 1-indexed labels
    
    returns the *shuffled* answers
    """
    print question
    for i,answer in enumerate(answers):
        print '    {}) {}'.format(i+1, answers[i])

def get_response():
    """Ask the user to make a choice
    
    returns 0-indexed result or None if the user enters nothing
    """
    try:
        return int(raw_input("Your answer? ")) - 1
    except Exception:
        return None

def run_level( level_number, level, errors, winnings ):
    question,correct,answers = level[0],level[1],level[1:]
    random.shuffle(answers)
    
    correct_answer = False
    while not correct_answer:
        display_status(level_number, winnings)
        display_questions( question,answers )
        response = get_response( )
        if response is None:
            # User has chosen to leave with current winnings
            print "Sorry to see you go!"
            raise SystemExit(0)
        chosen = answers[response]
        if chosen == correct:
            print "Correct!"
            winnings += reward(level_number)
            correct_answer = True
        else:
            errors += 1
            winnings = winnings//2
            if errors >= 3:
                print "WRONG!, Sorry, you've lost everything"%(errors,)
                winnings = 0
                raise SystemExit(1)
            else:
                print "WRONG!, %s Errors"%(errors,)
    return errors,winnings

def run_game():
    """Run the Trivia Game until the user exits, wins or loses"""
    errors = 0
    winnings = 0
    list_of_questions = load_questions()
    try:
        for level_number,level in enumerate(list_of_questions):
            errors,winnings = run_level( level_number, level, errors, winnings )
    except SystemExit:
        if winnings:
            print "Your winnings were ${}".format(winnings, )
        else:
            print "Please try again!"

#mainline_start
if __name__ == "__main__":
    run_game()
#mainline_stop
