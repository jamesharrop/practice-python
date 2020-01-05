'''
String Lists  
Exercise 6
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

import functools

strings = ["StriirtS", "Random"]

def is_a_palindrome_1(str) -> bool:
    is_a_palindrome = True

    for index, letter in enumerate(str):
        if letter != str[-index-1]:
            is_a_palindrome = False

    return is_a_palindrome

def is_a_palindrome_2(str) -> bool:
    return all([(str[-index-1] == letter) for index, letter in enumerate(str)])

def is_a_palindrome_3(str) -> bool:
     return (str == str[::-1])


for str in strings:
    print(f"Is {str} a palindrome?")
    print("Check using three different methods: ")
    print(is_a_palindrome_1(str))
    print(is_a_palindrome_2(str))
    print(is_a_palindrome_3(str))