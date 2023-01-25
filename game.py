import random


class Game:

    def __init__(self):
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    def _check_if_board_full(self):
        full_cells = 0

        for row in self.board:
            for item in row:
                if item != '_':
                    full_cells += 1

                if full_cells == 9:
                    return True
                else:
                    return False

    def _horizontal_win_check(self): #TODO parametrize by symbol using the player variable
        x_counter = 0
        o_counter = 0
        for i in range(len(self.board)):
            for item in self.board[i]:
                if item == "X":
                    x_counter += 1
                elif item == "O":
                    o_counter += 1
            if x_counter == 3:
                return 'We have a winner! Player 1 wins!'
            else:
                x_counter = 0
            if o_counter == 3:
                return 'We have a winner! Player 2 wins!'
            else:
                o_counter = 0

    def _vertical_win_check(self):
        x_counter = 0
        o_counter = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[j][i] == "X":
                    x_counter += 1
                elif self.board[j][i] == "O":
                    o_counter += 1
            if x_counter == 3:
                return 'We have a winner! Player 1 wins!'
            else:
                x_counter = 0
            if o_counter == 3:
                return 'We have a winner! Player 2 wins!'
            else:
                o_counter = 0

    def _diagonal_win_check(self):
        if self.board[1][1] == "X":
            if self.board[0][0] == "X" and self.board[2][2] == "X" or \
                    self.board[0][2] == "X" and self.board[2][0] == "X":
                return 'We have a winner! Player 1 wins!'
        elif self.board[1][1] == "O":
            if self.board[0][0] == "O" and self.board[2][2] == "O" or \
                    self.board[0][2] == "O" and self.board[2][0] == "O":
                return 'We have a winner! Player 2 wins!'

    def __str__(self):
        return '\n'.join(['  '.join(row) for row in self.board])

    def get_random_first_player(self): # TODO use random.choice instead of randint to choose from "X" or "O"
        return random.randint(0, 1)

    def swap_player_turn(self, player):
        return "X" if player == "O" else 'O'

    def validate_user_input(self, user_input):
        if user_input.isnumeric() and int(user_input) in range(1, 9):
            return True
        return False

    def get_row_and_col(self, user_input):
        row = (int(user_input) - 1) // 3
        column = (int(user_input) - 1) % 3
        return row, column

    def turn_sequence(self):

        player = "X" if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")
            print(self.__str__())

            user_defined_cell = input("Please select an index from 1 to 9 to place your symbol: ").strip()

            try:
                self.validate_user_input(user_defined_cell)
                row, col = self.get_row_and_col(user_defined_cell)
            except ValueError:
                print("Please enter a valid cell number 1 to 9!")
                continue

            # check whether cell is taken
            if not self.board[row][col] == "_":
                print("This cell is taken! Please enter new row and column indexes! ")
                continue
            self.board[row][col] = player

            # check whether win conditions are met #TODO change checks so they are not repeated
            if self._horizontal_win_check():
                print(self._horizontal_win_check())
                break
            elif self._diagonal_win_check():
                print(self._diagonal_win_check())
                break
            elif self._vertical_win_check():
                print(self._vertical_win_check())
                break

            # check whether board is full
            if self._check_if_board_full():
                print("Match Draw!")
                break
            # switch player
            player = self.swap_player_turn(player)
        print()
        print(self.__str__())


if __name__ == "__main__":
    game = Game()
    game.turn_sequence()
