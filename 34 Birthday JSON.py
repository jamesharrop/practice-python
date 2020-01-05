'''
Exercise 34
In the previous exercise we created a dictionary of famous scientists’ birthdays. 
In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, 
rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, 
and update the JSON file you have on disk with the scientist’s name. 
If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.
'''

import json
import pathlib

filename = "names_and_birthdays.json"

# Check, does the json file exist already, if not then create the file with some initial values
path = pathlib.Path(filename)
if not path.is_file():
    dict_initial = {
        "Joe": "1/2/1999",
        "Dave": "3/4/1995",
        "Mark": "12/5/2002"
        }
    with open(filename, "w") as f:
        json.dump(dict_initial, f)

# Then read in the file
with open(filename, "r") as f:
    dict = json.load(f)

# Add more data
new_name = input("Enter another name: ")
new_DOB = input("And the DOB: ") # We don't do any data validation

dict.update({new_name: new_DOB})

# Write the file
with open(filename, "w") as f:
    json.dump(dict, f)