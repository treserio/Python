'''Testing module for tic_tac_toe_v4.py
'''
import sys
import io
import unittest
from unittest.mock import patch
import tic_tac_toe_v4

class TestTicTacToe(unittest.TestCase):
    '''Testing all the functions used in tic_tac_toe_v4.py
    '''
    def test_clear_output(self):
        '''capture the print output and compare to expected values, print adds an extra \n
        '''
        capture = io.StringIO()
        sys.stdout = capture
        tic_tac_toe_v4.clear_output()
        sys.stdout = sys.__stdout__
        self.assertCountEqual(capture.getvalue(), '\n'*50)

    def test_board_draw(self):
        '''capture the print output and compare to expected values, print adds an extra \n
        '''
        capture = io.StringIO()
        sys.stdout = capture
        tic_tac_toe_v4.display_board()
        sys.stdout = sys.__stdout__
        compare = " 7 | 8 | 9 \n-----------\n 4 | 5 | 6 \n-----------\n 1 | 2 | 3 \n"
        self.assertEqual(capture.getvalue(), compare)

    # Trying to test player_input for unacceptable value results in a loop without user input
    @patch('builtins.input', return_value='x')
    def test_player_input_x(self, input):
        '''Testing player_input() for X
        '''
        result = tic_tac_toe_v4.player_input()
        self.assertEqual(result, 'X')

    @patch('builtins.input', return_value='o')
    def test_player_input_o(self, input):
        '''Testing player_input() for O
        '''
        result = tic_tac_toe_v4.player_input()
        self.assertEqual(result, 'O')

    def test_place_mark(self):
        '''Testing to ensure the board is edited in the correct position with the given mark
        '''
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        tic_tac_toe_v4.place_mark(board, "$", 0)
        compare = ["$", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.assertEqual(board, compare)

    # check the various win conditions
    def test_win_check_horizontal(self):
        '''Checking horizontal win
        '''
        board = ["X", "X", "X", "4", "5", "6", "7", "8", "9"]
        result = tic_tac_toe_v4.win_check(board, "X")
        self.assertEqual(result, True)

        board = ["1", "2", "3", "X", "X", "X", "7", "8", "9"]
        result = tic_tac_toe_v4.win_check(board, "X")
        self.assertEqual(result, True)

        board = ["1", "2", "3", "4", "5", "6", "X", "X", "X"]
        result = tic_tac_toe_v4.win_check(board, "X")
        self.assertEqual(result, True)

    def test_win_check_vertical(self):
        '''Checking vertical win
        '''
        board = ["X", "2", "3", "X", "5", "6", "X", "8", "9"]
        result = tic_tac_toe_v4.win_check(board, "X")
        self.assertEqual(result, True)

        board = ["1", "X", "3", "4", "X", "6", "7", "X", "9"]
        result = tic_tac_toe_v4.win_check(board, "X")
        self.assertEqual(result, True)

        board = ["1", "2", "X", "4", "5", "X", "7", "8", "X"]
        result = tic_tac_toe_v4.win_check(board, "X")
        self.assertEqual(result, True)

    def test_win_check_diagonal(self):
        '''Checking diagonal win
        '''
        board = ["X", "2", "3", "4", "X", "6", "7", "8", "X"]
        result = tic_tac_toe_v4.win_check(board, "X")
        self.assertEqual(result, True)

        board = ["1", "2", "X", "4", "X", "6", "X", "8", "9"]
        result = tic_tac_toe_v4.win_check(board, "X")
        self.assertEqual(result, True)

    def test_choose_first(self):
        '''Tests randomly returned string vs possible results
        '''
        result = tic_tac_toe_v4.choose_first()
        self.assertIn(result, ("1st", "2nd"))

    def test_space_check(self):
        '''Confirm if the position chosen is already occupied by a mark, testing True & False
        '''
        board = ["X", "2", "3", "4", "X", "6", "7", "8", "X"]
        result1 = tic_tac_toe_v4.space_check(board, 2)
        result2 = tic_tac_toe_v4.space_check(board, 0)
        self.assertEqual(result1, False)
        self.assertEqual(result2, True)

    def test_full_board_check(self):
        '''Confirm that a full board will result True
        '''
        board = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        result = tic_tac_toe_v4.full_board_check(board)
        self.assertEqual(result, True)

    @patch('builtins.input', return_value='3')
    def test_player_choice(self, input):
        '''Check that a valid input will return it's int() value -1
        '''
        board = ["X", "O", "3", "O", "X", "O", "X", "O", "X"]
        result = tic_tac_toe_v4.player_choice(board, "X")
        self.assertEqual(result, 2)

    @patch('builtins.input', return_value='y')
    def test_replay(self, input):
        '''Check the return value of player confirmation
        '''
        result = tic_tac_toe_v4.replay()
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
