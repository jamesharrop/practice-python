'''
Exercise 16
http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 

Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

import secrets
import string

def create_random_password():
    print("Make a password including all printable characters: ")
    length = int(input("How many characters do you want for the password? "))

    printable = string.printable
    whitespace = string.whitespace
    possible_chars = [x for x in printable if x not in whitespace]

    password = ""
    for _ in range(length):
        password = password + possible_chars[secrets.randbelow(len(possible_chars))]
    return password

def create_word_password():
    print("Make a password using words from the Scrabble dictionary: ")
    length = int(input("How many words do you want for the password? "))
    password = ""
    for _ in range(length):
        with open("sowpods.txt", "r") as f:
            word_list = f.readlines()
            word = secrets.choice(word_list).strip()
            password += word.lower() + "-"
    password = password.strip("-")
    return password

if __name__ == "__main__":
    print(create_random_password())
    print(create_word_password())
