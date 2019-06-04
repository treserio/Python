'''
Play TicTacToe in the console!
'''

import random
from IPython.display import clear_output
#Note that clear_output() will only work in jupyter.

#print('\n'*100) for clearing outside of jupyter

# function to display the TicTacToe Board
def display_board(board=None):
    '''Displays a single string with new line characters to setup the board.

    Args:
        board: a list of 8 strings corresponding to locations on a TicTacToe board.
    '''
    if board is None:
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    draw = f" {board[6]} | {board[7]} | {board[8]} "\
        f"\n-----------\n {board[3]} | {board[4]} | {board[5]} "\
        f"\n-----------\n {board[0]} | {board[1]} | {board[2]} "
    print(draw)

def player_input():
    '''Requests the players choice of mark and confirms it's a valid selection before
    returning the input in uppercase

    Returns:
        'X' or 'O'
    '''
    player1 = input("Please pick a mark 'X' or 'O': ")
    while player1.lower() not in ("x", "o"):
        player1 = input("Please enter an X or an O: ")

    return player1.upper()

def place_mark(board, mark, position):
    '''Places the current players mark in the selected position
    '''
    board[position] = mark

def win_check(board, mark):
    '''Checks for win conditions based on slices of the board list and returns bool

    Args:
        board: a list of 8 strings corresponding to locations on a TicTacToe board.
        mark: The char string of the current players mark
    '''
    #display_board(board)
    #print([mark, mark, mark]==board[:3])
    # Check horizontals using list comparisons vs slices of the board
    if [mark]*3 == board[:3] or [mark]*3 == board[3:6] or [mark, mark, mark] == board[6:]:
        #print("hori")
        return True
    # Check diagonal slices of the board using a for loop in all()
    if all(i == mark for i in board[0::4]) or all(i == mark for i in board[2:7:2]):
        #print("diag")
        return True
    # Check vertical slices of the board using a for loop in all()
    if (all(i == mark for i in board[0::3]) or all(i == mark for i in board[1::3]) or
            all(i == mark for i in board[2::3])):
        #print("vert")
        return True
    return False

def choose_first():
    '''This was part of the excersize, but it's just returning random.randint(0,1)
    '''
    return random.randint(0, 1)

def space_check(board, position):
    '''Confirm if the position chosen is already occupied by a mark
    '''
    return board[position] in ("X", "O")

def full_board_check(board):
    '''check all() values in the given list to see if a mark is already present

    Args:
        board: a list of 8 strings corresponding to locations on a TicTacToe board
    '''
    return all("X" in i or "O" in i for i in board)

def player_choice(board, mark):
    '''Confirms that player input is a num from 1-9 and corrects if needed before confirming that
    the selected move is available to make. Then returns the int form of the input.

    Args:
        board: a list of 8 strings corresponding to locations on a TicTacToe board
        mark: The char string of the current players mark

    Returns:
        The integer from (1-9)-1 that a player selected
    '''
    move = input(f"Please enter 1-9 for {mark}'s move: ")
    # Check that the entry is valid
    while move not in ('1', '2', '3', '4', '5', '6', '7', '8', '9') or move == "":
        move = input("Invalid, please choose number between 1 and 9: ")
    # check if move is available, if not request a new move
    while space_check(board, int(move)-1):
        move = input("That space is occupied, choose again: ")

    return int(move)-1

def replay():
    '''Checks if the players want to play another game anything other than a "y" will end the app.
    '''
    return input("Play again (Y/N): ").lower() == "y"

# begin the TicTacToe application using the above functions
# while playAgain = True play TicTacToe
PLAY_AGAIN = True
while PLAY_AGAIN:
    # display greeting
    clear_output()
    print('Welcome to TicTacToe!')

    BOARD = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # initialize player list
    PLAYERS = ["Plyr1", "Plyr2"]

    # The first player chooses their mark and it's assigned to a turn based on list location
    PLAYERS[choose_first()] = player_input()

    # Find out which mark was setup from the above call
    if PLAYERS[0] == "Plyr1":
        if PLAYERS[1] == "O":
            PLAYERS[0] = "X"
        else:
            PLAYERS[0] = "O"
    else:
        if PLAYERS[0] == "O":
            PLAYERS[1] = "X"
        else:
            PLAYERS[1] = "O"

    #print(PLAYERS)

    # show which mark goes first
    print(f"{PLAYERS[0]} will be the first player")

    # set turn keeper
    TURN = 0
    # while the board isn't full play the game
    while not full_board_check(BOARD):
        display_board(BOARD)
        # get the first players move, and using player_choice()
        # check if their selected move is valid
        place_mark(BOARD, PLAYERS[TURN], player_choice(BOARD, PLAYERS[TURN]))
        if win_check(BOARD, PLAYERS[TURN]):
            # clear the previous board and display new board with winning move
            clear_output()
            display_board(BOARD)
            print(f"Congratultions {PLAYERS[TURN]} You've Won!")
            break
        # clear previous entries
        clear_output()
        if TURN == 0:
            TURN = 1
        else:
            TURN = 0
    if full_board_check(BOARD) and not win_check(BOARD, PLAYERS[TURN]):
        print("Good Game! It's a Tie!")

    # check for rematch
    PLAY_AGAIN = replay()
print("Thank you for playing!")
