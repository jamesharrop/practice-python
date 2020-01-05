'''
Exercise 22
Given a .txt file that has a list of locations, count how many of each name there are in the file.

Sample line from .txt file:
/a/amusement_arcade/sun_afwazsrurvsdfsfdsf.jpg

Sample output:
Counter({'amusement_arcade': 50, 'amusement_park': 50})
'''

from collections import Counter

with open('2019_12_30 PracticePython\Training_01.txt', 'r') as f:
    lines = f.readlines()

lines = [x.strip("\n") for x in lines]
lines = [x[3:] for x in lines] # Remove the initial /a/
lines = [x.split("/")[0] for x in lines]

print(Counter(lines))