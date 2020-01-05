'''
A simple version of Tic Tac Toe using terminal input.
'''

from collections import namedtuple

BoardPosition = namedtuple('BoardPosition','row column')

class SuggestedMoveNotPossibleError(ValueError):
    # A custom error type
    pass

class Board:
    # Handles drawing the board, entering moves, checking who wins
    def __init__(self):
        self.game = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]

    def draw_board(self):
        columns = 3
        rows = 3
        def draw_horizontal_dividers(how_many):
            out = ""
            for _ in range(how_many):
                out += " ---"
            print(out)

        def draw_vertical_dividers(how_many, row):
            out = ""
            for column in range(how_many):
                out += "¦ "+ str(self.game[row][column]) + " "
            out += "¦"
            print(out)

        count = 0
        for row in range(rows):
            draw_horizontal_dividers(columns)
            draw_vertical_dividers(columns, count)
            count += 1

        draw_horizontal_dividers(columns)

    def make_a_move(self, player, move):
        if move.row < 0 or move.row > 2 or move.column < 0 or move.column > 2:
            raise SuggestedMoveNotPossibleError('Invalid move: that square is not on the board.')

        if self.game[move.row][move.column] == 0:
            self.game[move.row][move.column] = player.number
        else:
            raise SuggestedMoveNotPossibleError('Invalid move: that square is already taken.')

    def check_who_wins(self):
        # Returns int representing number of winning player, or zero if no winner
        def check_winner_for_3_squares(x: list):
            if x[0] == x[1] == x[2]:
                return x[0]
            return 0

        winner = []
        for row in self.game: # Rows
            winner.append(check_winner_for_3_squares(row))

        # Columns
        for column in range(3):
            x = [self.game[0][column], self.game[1][column], self.game[2][column]]
            winner.append(check_winner_for_3_squares(x))

        # Diagonals
        x = [self.game[0][0], self.game[1][1], self.game[2][2]]
        winner.append(check_winner_for_3_squares(x))
        x = [self.game[0][2], self.game[1][1], self.game[2][0]]
        winner.append(check_winner_for_3_squares(x))

        return sum(winner)

    def check_if_board_is_full(self):
        output = 1
        for row in self.game:
            for square in row:
                output *= square
        # If any zeros on board, i.e. empty squares -> then output = zero
        return output


class Player:
    # Handles interaction with players
    number_of_players = 0

    def __init__(self, name):
        Player.number_of_players += 1
        self.number = Player.number_of_players
        self.name = name

    def greet_player(self):
        print("Hello, ", self.name, ", you are player", self.number)

    def ask_for_a_move(self):
        row = int(input(f"{self.name}, which row? "))
        column = int(input(f"{self.name}, which column? "))
        move = BoardPosition(row = row-1, column = column-1) # Player should input row 1 to mean row 0
        return move
    
    def say_has_won(self):
        print(f"{self.name} has won.")

class TicTacToeGame:
    # Handles sequence of gameplay
    def __init__(self):
        self.players = [Player('Dave'), Player('Jane')]
        self.board = Board()
    
    def play_game(self):
        for player in self.players:
            player.greet_player()

        # Note: could probably simplify the flow here
        winner = 0
        while winner == 0 and not self.board.check_if_board_is_full():
            for player in self.players:
                while True: # Keep asking for a move until player enters a valid move
                    self.board.draw_board()
                    move = player.ask_for_a_move()
                    try:
                        self.board.make_a_move(player, move)
                    except SuggestedMoveNotPossibleError as err:
                        print(err) # Invalid move
                    else:
                        break # Valid move -> next player's turn
                winner = self.board.check_who_wins()
                if winner !=0:
                    break
                if self.board.check_if_board_is_full():
                    self.board.draw_board
                    print("It's a draw.")
                    exit()

        self.board.draw_board()
        self.players[winner-1].say_has_won()

if __name__ == "__main__":
    tictactoe = TicTacToeGame()
    tictactoe.play_game()