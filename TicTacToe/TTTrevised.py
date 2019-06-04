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
    while player1.lower() not in "xo":
        player1 = input("Please enter an X or an O: ")

    return player1.upper()

def place_mark(board, mark, position):
    '''Places the current players mark in the selected position
    '''
    board[position] = mark

def win_check(board, mark):
    '''Checks for win conditions based on slices of the board list

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
    '''Confirm if the position chosen is already occupied

    Returns:
        True if occupied
        False if open
    '''
    return board[position] in "XO"

def full_board_check(board):
    '''check all() values in the given list to see if a mark is already present

    Args:
        board: a list of 8 strings corresponding to locations on a TicTacToe board
    '''
    return all("X" in i or "O" in i for i in board)

def player_choice(board, mark):
    '''Confirms that player input is a num from 1-9 and corrects if needed before confirming that
    the selected move is available to make. Then returns the int of the input.

    Args:
        board: a list of 8 strings corresponding to locations on a TicTacToe board
        mark: The char string of the current players mark

    Returns:
        The integer from (1-9)-1 a player selected
    '''
    move = input(f"Please enter 1-9 for the {mark}'s move: ")
    # Check that the entry is valid
    while move not in ('1', '2', '3', '4', '5', '6', '7', '8', '9') or move == "":
        move = input("Invalid, please choose number between 1 and 9: ")
    # check if move is available, if not request a new move
    while space_check(board, int(move)-1):
        move = input("That space is occupied, choose again: ")

    return int(move)-1

def replay():
    '''Returns the truth value of input.lower() = "y"
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
    PLAYERS = []
    # append lists to use
    PLAYERS.append([0])
    PLAYERS.append([1])

    # Set first player and their mark
    PLAYERS[choose_first()].append(player_input())

    # find first player and their mark to set second player's mark, first player will now have a
    # len() == 2 because their mark was appended
    if len(PLAYERS[0]) == 2:
        if PLAYERS[0][1] == "X":
            PLAYERS[1].append("O")
        else:
            PLAYERS[1].append("X")
    else:
        if PLAYERS[1][1] == "X":
            PLAYERS[0].append("O")
        else:
            PLAYERS[0].append("X")

    #print(PLAYERS)

    # show which mark goes first
    if PLAYERS[0][0] == 0:
        print(f"The First player is {PLAYERS[0][1]}\n")
    else:
        print(f"The First player is {PLAYERS[1][1]}\n")

    # set turn keeper
    TURN = 0
    # while the board isn't full play the game
    while not full_board_check(BOARD):
        display_board(BOARD)
        # get the first players move, and using player_choice()
        # check if their selected move is valid
        place_mark(BOARD, PLAYERS[TURN][1], player_choice(BOARD, PLAYERS[TURN][1]))
        if win_check(BOARD, PLAYERS[TURN][1]):
            # clear the previous board and display new board with winning move
            clear_output()
            display_board(BOARD)
            print(f"Congratultions {PLAYERS[TURN][1]} You've Won!")
            break
        # clear previous entries
        clear_output()
        if TURN == 0:
            TURN = 1
        else:
            TURN = 0
    if full_board_check(BOARD) and not win_check(BOARD, PLAYERS[TURN][1]):
        print("Good Game! It's a Tie!")

    # check for rematch
    PLAY_AGAIN = replay()
print("Thank you for playing!")
