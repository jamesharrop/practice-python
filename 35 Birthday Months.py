'''
Birthday Months  
Exercise 35 from practicepython.org

In the previous exercise we saved information about famous scientists’ names and birthdays to disk. 
In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.
'''

import json
from datetime import datetime
import calendar
from collections import Counter

filename = "names_and_birthdays.json"

with open(filename, "r") as f:
    dict = json.load(f)

months = []
for person in dict:
    date = datetime.strptime(dict[person], "%d/%m/%Y")
    months.append(calendar.month_name[date.month])

c = Counter(months)

print(c)
