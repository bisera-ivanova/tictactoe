import game
import unittest
import random


class GameTest(unittest.TestCase):
    game_class = game.Game()

    def test_horizontal_win_check(self):
        board1 = [["X", "X", "X"], ["_", "_", "_"], ["_", "_", "_"]]
        board2 = [["_", "_", "_"], ["_", "_", "_"], ["O", "O", "O"]]
        player_symbol1 = "X"
        player_symbol2 = "O"

        expected_output1 = True
        expected_output2 = None

        game_class = game.Game()
        game_class.board = board1
        actual_output1 = game_class._horizontal_win_check(player_symbol1)
        actual_output2 = game_class._horizontal_win_check(player_symbol2)

        game_class.board = board2
        actual_output3 = game_class._horizontal_win_check(player_symbol2)
        actual_output4 = game_class._horizontal_win_check(player_symbol1)

        self.assertEqual(expected_output1, actual_output1)
        self.assertEqual(expected_output2, actual_output2)
        self.assertEqual(expected_output1, actual_output3)
        self.assertEqual(expected_output2, actual_output4)

    def test_vertical_check(self):
        board1 = [["X", "_", "_"], ["X", "_", "_"], ["X", "_", "_"]]
        board2 = [["_", "_", "_"], ["_", "_", "_"], ["O", "O", "O"]]
        player_symbol1 = "X"
        player_symbol2 = "O"

        expected_output1 = True
        expected_output2 = None

        game_class = game.Game()
        game_class.board = board1
        actual_output1 = game_class._vertical_win_check(player_symbol1)
        actual_output2 = game_class._vertical_win_check(player_symbol2)

        game_class.board = board2
        actual_output3 = game_class._vertical_win_check(player_symbol1)
        actual_output4 = game_class._vertical_win_check(player_symbol2)

        self.assertEqual(expected_output1, actual_output1)
        self.assertEqual(expected_output2, actual_output2)
        self.assertEqual(expected_output2, actual_output3)
        self.assertEqual(expected_output2, actual_output4)

    def test_diagonal_win_check(self):
        board1 = [["X", "_", "_"], ["_", "X", "_"], ["_", "_", "X"]]
        board2 = [["O", "_", "_"], ["O", "_", "_"], ["_", "_", "O"]]
        player_symbol1 = "X"
        player_symbol2 = "O"

        expected_output1 = True
        expected_output2 = None

        game_class = game.Game()
        game_class.board = board1
        actual_output1 = game_class._diagonal_win_check(player_symbol1)
        actual_output2 = game_class._diagonal_win_check(player_symbol2)

        game_class = game.Game()
        game_class.board = board2
        actual_output3 = game_class._diagonal_win_check(player_symbol1)
        actual_output4 = game_class._diagonal_win_check(player_symbol2)

        self.assertEqual(expected_output1, actual_output1)
        self.assertEqual(expected_output2, actual_output2)
        self.assertEqual(expected_output2, actual_output3)
        self.assertEqual(expected_output2, actual_output4)

    def test_get_random_first_player(self):
        game_class = game.Game()
        random.seed(0)
        self.assertEqual(game_class._get_random_first_player(), "O")

    def test_validate_user_input(self):
        expected_outcome_true = True
        expected_outcome_false = None

        sample_input1 = "7"
        sample_input2 = "asd"
        sample_input3 = "10"
        sample_input4 = "True"
        game_class = game.Game()
        actual_output1 = game_class._validate_user_input(sample_input1)
        actual_output2 = game_class._validate_user_input(sample_input2)
        actual_output3 = game_class._validate_user_input(sample_input3)
        actual_output4 = game_class._validate_user_input(sample_input4)

        self.assertEqual(expected_outcome_true, actual_output1)
        self.assertEqual(expected_outcome_false, actual_output2)
        self.assertEqual(expected_outcome_false, actual_output3)
        self.assertEqual(expected_outcome_false, actual_output4)

    def test_get_row_and_col(self):
        game_class = game.Game()
        sample_input = "8"
        expected_output = (2, 1)
        actual_output = game_class._get_row_and_col(sample_input)

        self.assertEqual(expected_output, actual_output)

    def test_play_game(self):
        expected_output = """
        Player X turn
        _  _  _
        _  _  _
        _  _  _
        Please select an index from 1 to 9 to place your symbol:"""
        game_class = game.Game()
        actual_output = game_class.play_game()
        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    test = GameTest()
