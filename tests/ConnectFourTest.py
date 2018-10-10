import sys
sys.path.append('../')
from scripts.play_connect_four import get_current_player, \
                                      is_state_valid, \
                                      play,get_winner
import unittest
from pprint import pprint
from random import randrange


class ConnectFourTest(unittest.TestCase):

    def setUp(self):
        self.blank_game_state = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]
        self.test_game_state_1 = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, "y", "r", None, None, None],
            [None, None, "r", "y", None, None, None],
            ["r", "y", "y", "y", "r", "r", "y"],
            ["r", "r", "y", "y", "r", "y", "r"],
        ]

    def test_play_connect_four_1(self):

        self.connect_four_tester(self.test_game_state_1)

    # def test_play_connect_four_blank(self):
    #     self.connect_four_tester(self.blank_game_state)

    def connect_four_tester(self, game_state):
        """
        This function plays a game of connect_four until there is a winner.
            If there is an issue trying to play a column the script will retry
            playing with a different column number.
        :param game_state:
        :return:
        """
        winner = False
        turns = 0
        while not winner:
            print ("------------------------")
            turns += 1
            player = get_current_player(game_state)
            print ("TURN --- {} - Player - {} ".format(turns, player))
            print ("-------------------------")
            pprint(game_state)
            column = randrange(len(game_state[0]))
            temp_game_state = play(game_state, column, player)
            if temp_game_state == "Bad selection, please try another column!":
                print ("Trying another column")
                continue
            else:
                game_state = temp_game_state

            self.assertEqual(is_state_valid(game_state), True)
            winner = get_winner(game_state)

        self.assertEqual(winner, True)
        print("We have a winner!")
        print("Number of Turns - {}".format(turns))
        print("------------------------------")
        pprint(game_state)


if __name__ == '__main__':
    unittest.main()
