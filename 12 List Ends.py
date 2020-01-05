'''
Exercise 12
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
'''

def first_and_last(a):
    """
    Finds first and last elements in a list

    Args:
        a: the list

    Returns:
        The first and last elements in the list

    Raises:
        IndexError: if passed an empty list
        TypeError: if passed an object which is not a list
    """
    if not isinstance(a, list):
        raise TypeError

    if len(a) < 2:
        raise IndexError

    return [a[0],a[-1]]


a = [5, 10, 15, 20, 25]
print(first_and_last(a))