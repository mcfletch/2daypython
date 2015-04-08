import random, time, os
random.seed(time.time())

HERE = os.path.dirname(__file__)
DEFAULT_QUESTIONS = os.path.join(HERE, 'questions.txt')

def read_line(line):
    """Process a single line from the questions"""
    line = line.strip()
    line = line.split('|')
    return line

def load_questions(filename=DEFAULT_QUESTIONS):
    """Load our questions from the filename
    
    Format of the file:
    
        question|answer|bad_answer|bad_answer...
    """
    questions = []
    for line in open(filename):
        questions.append(read_line(line))
    return questions

def reward( level_number ):
    """Reward should double for each level starting at 1000"""
    return 2**level_number * 1000

def display_status( level_number,  winnings ):
    print "Level %i for $%i    Current winnings: $%i"%(
        level_number+1, 
        reward(level_number), 
        winnings,
    )

def display_questions( level ):
    
    question, order = level[0], level[1:]
    random.shuffle(order)
    
    print question
    for i in range(len(order)):
        print '    %i %s'%(i+1, order[i])
    
    return order
    
def get_response():
    try:
        return int(raw_input("Your answer? ")) - 1
    except Exception:
        return None

def run_game():
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
            print "Sorry, the correct answer was: %s"%(level[1])
            break
    print "Your winnings were $%s"%(winnings, )
        
if __name__ == "__main__":
    run_game()
