'''
Birthday Dictionaries
Exercise 33 from practicepython.com

Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 
'''

dict = {
    "Joe": "1/2/1999",
    "Dave": "3/4/1995",
    "Mark": "12/5/2002"
    }

print('Welcome to the birthday dictionary. We know the birthdays of: ')
for name in dict.keys():
    print(name)

name_to_lookup = input("Who's birthday do you want to look up? ")

if name_to_lookup in dict:
    print(f"{name_to_lookup}'s birthday is {dict[name_to_lookup]}")
else:
    print("We don't know that one")