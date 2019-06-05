'''Testing module for tic_tac_toe_v4.py
'''

import unittest
import tic_tac_toe_v4

class TestTicTacToe(unittest.TestCase):

    def test_player_input(self):
        '''Steps, input x then input o
        '''
        result1 = tic_tac_toe_v4.player_input()
        result2 = tic_tac_toe_v4.player_input()

        self.assertEqual(result1, 'X')
        self.assertEqual(result2, "O")
