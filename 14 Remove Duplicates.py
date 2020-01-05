'''
List Remove Duplicates  
Exercise 14
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
'''

def remove_duplicates(a_list: list) -> list:
    output: list = []
    for element in a_list:
        if element not in output:
            output.append(element)
    return(output)

def remove_duplicates_2(a_list) -> list:
    # This method uses Sets but the order is lost
    output = list(set(a_list))
    return(output)

sample_list = [10, 2, 3, 2]
print(remove_duplicates(sample_list))
print(remove_duplicates_2(sample_list))