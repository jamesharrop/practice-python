# 5 List Overlap
# Three different ways to find intersection of two random lists, with duplicates removed

import random

def random_list():
    return list(random.randint(0, 100) for x in range(0, random.randint(0, 100)))

def list_overlap1(list_1, list_2):
    output=[]
    for element in list_1:
        if element in list_2:
            if element not in output: # Ignore duplicates
                output.append(element)
    return output

def list_overlap2(list_1, list_2):
    return list(set(x for x in list_1 if x in list_2))

def list_overlap3(list_1, list_2):
    return list(set(list_1).intersection(set(list_2)))

random_list_1 = random_list()
random_list_2 = random_list()

print(list_overlap1(random_list_1, random_list_2))
print(list_overlap2(random_list_1, random_list_2))
print(list_overlap3(random_list_1, random_list_2))