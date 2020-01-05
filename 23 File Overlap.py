'''
File Overlap  
Exercise 23
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
'''
def read_from_file(filename: str) -> list:
    with open(filename, 'r') as f:
        output = f.readlines()
    output = [x.strip("\n ") for x in output]
    return [int(x) for x in output]

primes = read_from_file('primenumbers.txt')
happy = read_from_file('happynumbers.txt')

result = set(primes).intersection(set(happy))
print(result)