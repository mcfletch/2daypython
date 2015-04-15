import random, time, os
random.seed(time.time())

#read_file_start
import os
HERE = os.path.dirname(__file__)
DEFAULT_QUESTIONS = os.path.join(HERE, 'questions.txt')

def load_questions(filename=DEFAULT_QUESTIONS):
    """Load our questions from the filename
    
    Format of the file:
    
        question|answer|bad_answer|bad_answer...
    """
    questions = []
    for line in open(filename):
        questions.append(read_line(line))
    return questions

def read_line(line):
    """Process a single line from the questions"""
    line = line.strip()
    line = line.split('|')
    return line

#read_file_stop

#reward_start
def reward( level_number ):
    """Reward should double for each level starting at 1000"""
    return 2**level_number * 1000
#reward_stop

def display_status( level_number,  winnings ):
    print "Level {} for ${}    Current winnings: ${}".format(
        level_number+1, 
        reward(level_number), 
        winnings,
    )

def display_questions( level ):
    """Display the question and the shuffled answers
    
    * shuffles the answers randomly
    * displays the answers with 1-indexed labels
    
    returns the *shuffled* answers
    """
    question, order = level[0], level[1:]
    random.shuffle(order)
    
    print question
    for i in range(len(order)):
        print '    {}) {}'.format(i+1, order[i])
    
    return order

def get_response():
    """Ask the user to make a choice
    
    returns 0-indexed result or None if the user enters nothing
    """
    try:
        return int(raw_input("Your answer? ")) - 1
    except Exception:
        return None

def run_game():
    """Run the Trivia Game until the user exits, wins or loses"""
    winnings = 0
    for level_number,level in enumerate(load_questions()):
        display_status(level_number, winnings)
        order = display_questions( level )
        response = get_response( )
        if response is None:
            break
        if order[response] == level[1]:
            winnings += reward(level_number)
        else:
            winnings = 0
            print "Sorry, the correct answer was: {}".format(level[1])
            break
    print "Your winnings were ${}".format(winnings, )
        
if __name__ == "__main__":
    run_game()
