'''
Exercise 24 from practicepython.org
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
'''

def draw_board(columns, rows):
    def draw_horizontal_dividers(how_many):
        out = ""
        for _ in range(how_many):
            out += " ---"
        print(out)

    def draw_vertical_dividers(how_many):
        out = ""
        for _ in range(how_many):
            out += "¦   "
        out += "¦"
        print(out)

    for row in range(rows):
        draw_horizontal_dividers(columns)
        draw_vertical_dividers(columns)

    draw_horizontal_dividers(columns)

if __name__ == "__main__":
    columns = int(input("How many columns? "))
    rows = int(input("How many rows? "))
    draw_board(columns, rows)