'''
Exercise 9 from http://www.practicepython.org/
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random

generated_number = random.randint(1, 9)
number_of_guesses = 0

while True:
    user_input = input("Guess a number between 1 and 9 inclusive, or type exit: ")

    if user_input == 'exit':
        break
    else:
        user_number = int(user_input)
        number_of_guesses += 1

    if user_number < generated_number:
        print("Too low")

    if user_number > generated_number:
        print("Too high")

    if user_number == generated_number:
        print("Just right")
        break

print(f"You had {number_of_guesses} guesses.")
