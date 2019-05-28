import random
from IPython.display import clear_output
#Note that clear_output() will only work in jupyter.

print('\n'*100)

def display_board(board = ['1','2','3','4','5','6','7','8','9',]):
    draw = f" {board[6]} | {board[7]} | {board[8]} \n-----------\n {board[3]} | {board[4]} | {board[5]} \n-----------\n {board[0]} | {board[1]} | {board[2]} "
    print(draw)

def player_input():
    player1 = input("Please pick a marker 'X' or 'O': ")
    while player1.lower() not in "xo":
        player1 = input("Please enter an X or an O: ")

    return player1

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    display_board(board)
    #print([mark,mark,mark]==board[:3])
    # Check horizontals
    if [mark,mark,mark] == board[:3] or [mark,mark,mark] == board[3:6] or [mark,mark,mark] == board[6:]:
        #print("hori")
        return True
    # Check diagonals
    elif all(i==mark for i in board[0::4]) or all(i==mark for i in board[2:7:2]):
        #print("diag")
        return True
    # Check Verticals
    elif all(i==mark for i in board[0::3]) or all(i==mark for i in board[1::3]) or all(i==mark for i in board[2::3]):
        #print("vert")
        return True

def choose_first():
    return random.randint(0,1)

def space_check(board, position):
    return board[position] not in "XO"

def full_board_check(board):
    return all("X" in i or "O" in i for i in board)

def player_choice(board, marker):
    move = input(f"Please enter 1-9 for the {marker}'s move: ")
    # Check that the entry is valid
    while move not in "123456789":
        move = input("Invalid, please choose number between 1 and 9: ")
    # check if move is available    
    while not space_check(board, int(move)-1):
        move = input("That space is occupied, choose again: ")

    return int(move)-1

def replay():
    return input("Play again (Y/N): ").lower() == "y"

clear_output()
print('Welcome to Tic Tac Toe!')

playAgain = True
while playAgain == True:
    board = ['1','2','3','4','5','6','7','8','9']
    
    # initialize player list
    players = []
    # append lists to use
    players.append([0])
    players.append([1])

    # Set first player and their mark
    players[choose_first()].append(player_input().upper())

    if len(players[0]) == 2:
        if players[0][1] == "X":
            players[1].append("O")
        else:
            players[1].append("X")
    else:
        if players[1][1] == "X":
            players[0].append("O")
        else:
            players[0].append("X")

    #print(players)
    if players[0][1].lower() == "x":
        players[1][1] = "O"
    else:
        players[1][1] = "X"
    
    # show which mark goes first
    if players[0][0] == 0:
        print(f"The First player is {players[0][1]}\n")
    else:
        print(f"First player is {players[1][1]}\n")

    display_board()
    # set turn keeper
    turn = 0
    # while the board isn't full play the game
    while full_board_check(board) == False:
        # get the first players move, and using player_choice() to check if their selected move is valid
        place_marker(board,players[turn][1],player_choice(board, players[turn][1]))
        display_board(board)
        clear_output()
        if win_check(board, players[turn][1]):
            print(f"Congratultions {players[turn][1]} You've Won!")
            break
            
        if turn == 0:
            turn = 1
        else:
            turn = 0

    # check for rematch
    playAgain = replay()
print("Thank you for playing!")