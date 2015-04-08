import random, time, os
random.seed(time.time())

HERE = os.path.dirname(__file__)
DEFAULT_QUESTIONS = os.path.join(HERE, 'questions.txt')

def load_questions(filename=DEFAULT_QUESTIONS):
    """Load our questions from the filename
    
    Format of the file:
    
        question|answer|bad_answer|bad_answer...
    """
    questions = []
    for line in open(filename):
        line = line.strip()
        if not line:
            continue 
        line = line.split("|")
        questions.append(line)
    return questions

def reward( level_number ):
    """Reward should double for each level starting at 1000"""
    return 2**level_number * 1000

def display( level_number,  level, winnings ):
    
    question, order = level[0], level[1:]
    random.shuffle(order)
    template = '''Level %s for $%s   Current winnings: $%s
%s
%s'''
    formatted = "\n".join(['  %i %s'%(i, answer) for i, answer in enumerate(order)])
    print template%( level_number+1, reward(level_number), winnings, question, formatted)
    return order
def get_response():
    try:
        return int(raw_input("Your answer? "))
    except Exception:
        return None

def run_game():
    winnings = 0
    for level_number,level in enumerate(load_questions()):
        order = display( level_number, level, winnings )
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
