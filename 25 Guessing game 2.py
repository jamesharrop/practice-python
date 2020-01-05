'''
Guessing Game Two   
Exercise 25 
http://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
'''
number_of_guesses = 0
current_guess = 50
lower_bound = 0
upper_bound = 100
while True:
    result = input(f"Is you number {current_guess}? (enter H: for No, too high; L: for No, too low; Y for yes): ")
    number_of_guesses += 1
    if result == "Y":
        print(f"I had {number_of_guesses} guesses.")
        break
    if result == "H":
        upper_bound = current_guess
        current_guess = int(lower_bound + (current_guess - lower_bound)/2)
    if result == "L":
        lower_bound = current_guess
        current_guess = int(current_guess+(upper_bound - current_guess)/2)

# Another option would be to use a list of numbers and trim the list as lower_bound and upper_bound change