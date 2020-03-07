'''
1
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will
turn 100 years old.
'''
import datetime

name = input("What is your name? ")
age = input("What is your age? ")
age = int(age)

bday = input("Have you had your birthday yet this year (Y/N)? ")
if bday == 'Y':
    offset = 0
else:
    offset = -1 

current_year = datetime.datetime.now().year
predicted_year = 100 - age + current_year + offset

print(f"Hi {name}, you will turn 100 in {predicted_year}.")