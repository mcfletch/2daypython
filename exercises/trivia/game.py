import random, time
random.seed(time.time())
LEVELS = [
    (
        "Who was the first Prime Minister of Canada?",
        [
            "Sir John Alexander Macdonald",
            "Lester B. Pearson",
            "Guglielmo Marconi",
            "Avril Lavigne",
            "Pierre Elliott Trudeau",
        ],
    ),
    (
        "What is the captial of Nunavut?",
        [
            "Iqaluit",
            "Alaska",
            "Red Deer",
            "Montreal",
            "St. Johns",
        ],
    ),
    (
        "What is the largest animal of all time?", 
        [
            "Blue Whale", 
            "Argentinosaurus", 
            "African Elephant", 
            "Whale Shark", 
            "Megalodon", 
        ], 
    ), 
]

def reward( level ):
    return 2**level * 1000

def display( level,  question,  answers, winnings ):
    order = answers[:]
    random.shuffle(order)
    template = '''Level %s for $%s   Current winnings: $%s
%s'''
    formatted = "\n".join(['  %i %s'%(i, answer) for i, answer in enumerate(order)])
    print template%( level+1, reward(level), winnings,  formatted)
    return order
def get_response():
    try:
        return int(raw_input("Your answer? "))
    except Exception:
        return None

def run_game():
    winnings = 0
    for level,(question,answers) in enumerate(LEVELS):
        order = display( level, question, answers, winnings )
        response = get_response( )
        if response is None:
            break
        if order[response] == answers[0]:
            winnings += reward(level)
        else:
            winnings = 0
    print "Your winnings were $%s"%(winnings, )
        
if __name__ == "__main__":
    run_game()
