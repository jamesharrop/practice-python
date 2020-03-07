'''
Exercise 8 from http://www.practicepython.org/
Make a two-player Rock-Paper-Scissors game. 
'''

class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.player_won = False

    def get_player_input(self):
        allowed_inputs = ['rock', 'paper', 'scissors']
        self.player_input = []        
        while self.player_input not in allowed_inputs:
            print(f'Player {self.player_number} input (enter rock, paper or scissors): ', end='')
            self.player_input = input()

p1 = Player(1)
p1.get_player_input()

p2 = Player(2)
p2.get_player_input()

if p1.player_input == p2.player_input:
    print("Draw")

if p1.player_input == 'rock': 
    if p2.player_input == 'scissors':
        p1.player_won = True
    if p2.player_input == 'paper':
        p2.player_won = True
elif p1.player_input == 'paper': 
    if p2.player_input == 'scissors':
        p2.player_won = True
    if p2.player_input == 'rock':
        p1.player_won = True
elif p1.player_input == 'scissors': 
    if p2.player_input == 'rock':
        p2.player_won = True
    if p2.player_input == 'paper':
        p1.player_won = True

if p1.player_won:
    print("Player 1 won")
if p2.player_won:
    print("Player 2 won")