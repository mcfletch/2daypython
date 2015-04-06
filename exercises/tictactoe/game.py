SIDES = ['X', 'O']

def print_board( board ):
    result = []
    for i, row in enumerate(board):
        row_description = []
        for j, value in enumerate(row):
            if value is None:
                row_description.append(' %s '%(j+i*3))
            else:
                row_description.append(' %s '%(SIDES[value]))
        row_description = ' | '.join( row_description )
        result.append( row_description )
    return "\n".join(result)

def rows(board):
    for row in board:
        yield row 
def cols(board):
    for i in range(3):
        yield [row[i] for row in board]
def diagonals(board):
    for indices in [
        [(0, 0), (1, 1), (2, 2)], 
        [(2, 0), (1, 1), (0, 2)], 
    ]:
        yield [ board[y][x] for (x, y) in indices ]

def all_one( line ):
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
    for row in rows(board):
        if all_one(row):
            return True 
    for col in cols(board):
        if all_one(col):
            return True
    for diag in diagonals(board):
        if all_one(diag):
            return True
    return False

board = [
    [None, None, None], 
    [None, None, None], 
    [None, None, None], 
]


def read_coordinate( board, side ):
    while True:
        move = raw_input( "%s's Move x,y: "%(SIDES[side], ) )
        move = int(move)
        x = move % 3
        y = move // 3
        if board[y][x] is None:
            return x,y
        else:
            print( "That index is assigned: %s, %s"%(x, y))

def play_game(board):
    current_move = 0
    while not finished(board):
        print print_board(board)
        x, y = read_coordinate( board, current_move )
        board[y][x] = current_move
        current_move = (current_move + 1) %2
    print print_board(board)

assert all_one([1, 1, 1])
assert all_one([0, 0, 0])
assert list(diagonals( [[0, 1, 2], [3, 4, 5], [6, 7, 8]])) == [[0, 4, 8], [2, 4, 6]]

if __name__ == "__main__":
    play_game(board)
