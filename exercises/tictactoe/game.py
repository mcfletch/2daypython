SIDES = ['X', 'Y']
board = [None]*9
WINNING_LINES = [
    [0, 1, 2], 
    [3, 4, 5], 
    [6, 7, 8], 
    [0, 3, 6], 
    [1, 4, 7], 
    [2, 5, 8], 
    [0, 4, 8], 
    [2, 4, 6], 
]

def print_board( board ):
    result = []
    for i in range(3):
        row_description = []
        for j in range(3):
            value = board[j+i*3]
            if value is None:
                row_description.append(' %s '%(j+i*3))
            else:
                row_description.append(' %s '%(SIDES[value]))
        row_description = ' | '.join( row_description )
        result.append( row_description )
    return "\n".join(result)

def winning( line ):
    current = None
    for item in line:
        if item is None:
            return False 
        elif current is None:
            current = item 
        elif current != item:
            return False 
    return True

def finished( board ):
    for set in WINNING_LINES:
        if winning([board[i] for i in set]):
            return True
    return False

def read_coordinate( board, side ):
    while True:
        move = raw_input( "%s's Move: "%(SIDES[side], ) )
        move = int(move)
        if board[move] is None:
            return move
        else:
            print( "That index is assigned: %s"%(move, ))

def play_game(board):
    current_move = 0
    while not finished(board):
        print print_board(board)
        move = read_coordinate( board, current_move )
        board[move] = current_move
        current_move = (current_move + 1) %2
    print print_board(board)

if __name__ == "__main__":
    play_game(board)
