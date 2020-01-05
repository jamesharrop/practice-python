'''
Check Tic Tac Toe  
Exercise 26 from practicepython.org

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	    [2, 1, 0],
	    [2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

Given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. '''

def check_who_wins(game):

    def check_winner_for_3_squares(x: list):
        if x[0] == x[1] == x[2]:
            return x[0]
        return 0

    winner = []
    # Rows
    for row in game:
        winner.append(check_winner_for_3_squares(row))

    # Columns
    for column in range(3):
        x = [game[0][column], game[1][column], game[2][column]]
        winner.append(check_winner_for_3_squares(x))

    # Diagonals
    x = [game[0][0], game[1][1], game[2][2]]
    winner.append(check_winner_for_3_squares(x))
    x = [game[0][2], game[1][1], game[2][0]]
    winner.append(check_winner_for_3_squares(x))

    if sum(winner) == 0:
        print("Draw")
    else:
        print(f"Player {sum(winner)} won.")

if __name__ == "__main__":
    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]

    check_who_wins(game)