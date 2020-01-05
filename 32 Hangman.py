'''
>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E

'''
'''
Psuedocode approach with assignment to objects:

Welcome message [Player]
Choose a random word [Board]
Display the word with _ symbols where no letters are known [Board]
Display how many guesses the player has left [Player]
Ask for a guess [Player]
Check whether the player has guessed that already - if so they get another go [Player]
Check whether that guess is in the word [Board]
Loop until word is guessed or guesses are all used up [Main]
'''

import random

class Player:
    def __init__(self):
        print("Welcome to this game.")
        self.guesses = []
        self.guesses_left = 6
    
    def print_how_many_guesses_left(self):
        if self.guesses_left>1:
            print(f"You have {self.guesses_left} guesses left.")
        else:
            print(f"You have {self.guesses_left} guess left.")

    def ask_for_guess(self) -> str:
        guess = input("Guess a letter: ").upper()
        if guess in self.guesses:
            return None
        self.guesses.append(guess)
        return guess

    def display_whether_guess_correct(self, correct: bool):
        if correct:
            print("Correct")
        else:
            print("That's not in the word")
    
    def print_message(self, message):
        print(message)

class Board:
    def __init__(self):
        self.word = ""
        self.guessed = [] # A list of Bools corresponding to which letters in word have been guessed

    def choose_random_word(self):
        with open("sowpods.txt", "r") as f:
            word_list = f.readlines()
            self.word = random.choice(word_list).strip()
            self.guessed = [False] * len(self.word)

    def display_word(self):
        for index, letter in enumerate(self.word):
            if self.guessed[index]:
                print(letter, end="")
            else:
                print("_", end="")
            print(" ", end="")
        print("\n")
    
    def check_if_guess_in_word(self, guess):
        is_in_word = False
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.guessed[index] = True
                is_in_word = True
        return(is_in_word)

    def all_letters_have_been_guessed(self):
        return (not any(letter == False for letter in self.guessed))

    def debug_print_out_variables(self):
        print("word:", self.word)
        print("guessed:", self.guessed)

if __name__ == "__main__":    
    print("\n")
    p = Player()
    b = Board()
    b.choose_random_word()

    while True:
        b.display_word()
        # b.debug_print_out_variables()
        while True:
            p.print_how_many_guesses_left()
            guess = p.ask_for_guess()
            if guess is None:
                p.print_message("You already guessed that letter - have another go")
            else:
                break
        correct = b.check_if_guess_in_word(guess)
        print("\n")
        p.display_whether_guess_correct(correct)
        if not correct:
            p.guesses_left -= 1
        if b.all_letters_have_been_guessed():
            p.print_message("All guessed")
            break
        if p.guesses_left == 0:
            p.print_message("All guesses used up")
            break

p.print_message(f"The word was: {b.word}")