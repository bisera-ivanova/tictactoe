import random


class Game:

    def __init__(self):
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.player_symbol = "X"
        self.turn_counter = 0
        self.play_game()

    def _horizontal_win_check(self, player_symbol):
        counter = 0
        for i in range(len(self.board)):
            for item in self.board[i]:
                if item == player_symbol:
                    counter += 1
            if counter == 3:
                return True
            else:
                counter = 0

    def _vertical_win_check(self, player_symbol):
        counter = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[j][i] == player_symbol:
                    counter += 1
            if counter == 3:
                return True
            else:
                counter = 0

    def _diagonal_win_check(self, player_symbol):
        if self.board[1][1] == player_symbol:
            if self.board[0][0] == player_symbol and self.board[2][2] == player_symbol or \
                    self.board[0][2] == player_symbol and self.board[2][0] == player_symbol:
                return True

    def __str__(self):
        return '\n'.join(['  '.join(row) for row in self.board])

    def _get_random_first_player(self):
        return random.choice(["X", "O"])

    def _swap_player_turn(self, player):
        return "X" if self.player_symbol == "O" else 'O'

    def _validate_user_input(self, user_input):
        if user_input.isnumeric() and int(user_input) in range(1, 9):
            return True
        return False

    def _get_row_and_col(self, user_input):
        row = (int(user_input) - 1) // 3
        column = (int(user_input) - 1) % 3
        return row, column

    def play_game(self):

        self.player_symbol = self._get_random_first_player()
        while self.turn_counter < 9:
            print(f"Player {self.player_symbol} turn")
            print(self.__str__())

            user_defined_cell = input("Please select an index from 1 to 9 to place your symbol: ").strip()

            try:
                self._validate_user_input(user_defined_cell)
                row, col = self._get_row_and_col(user_defined_cell)
            except ValueError:
                print("Please enter a valid cell number 1 to 9!")
                continue

            # check whether cell is taken
            if not self.board[row][col] == "_":
                print("This cell is taken! Please enter new row and column indexes! ")
                continue
            self.board[row][col] = self.player_symbol

            # check whether win conditions are met
            horizontal_check = self._horizontal_win_check(self.player_symbol)
            vertical_check = self._vertical_win_check(self.player_symbol)
            diagonal_check = self._diagonal_win_check(self.player_symbol)

            if horizontal_check or vertical_check or diagonal_check:
                print(f'We have a winner! Player {self.player_symbol} wins!')
                break

            # increment turn counter
            self.turn_counter += 1

            # switch player
            self.player_symbol = self._swap_player_turn(self.player_symbol)

        if self.turn_counter == 9:
            print("Match Draw!")
        print()
        print(self.__str__())


if __name__ == "__main__":
    game = Game()

