'''
Pick Word  
Exercise 30 - from http://www.practicepython.org/exercise/2016/09/24/30-pick-word.html

The task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. 
'''

import random

word_list = []

with open("sowpods.txt", "r") as f:
    word_list = f.readlines()

a = random.choice(word_list).strip()
print(a)