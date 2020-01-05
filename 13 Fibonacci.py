'''
13. Fibonacci
Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
'''

how_many = int(input("How many Fibonacci numbers to generate? "))

print("Iterative method")
def next_fibonacci(a, b):
    return b, (a + b)

a = b = 1
for x in range(how_many):
    print(a)
    a, b = next_fibonacci(a, b)

print("Recursive method")
def fibonacci(a, b, count):
    global how_many
    if count < how_many:
        print(a)
        return fibonacci(b, (a + b), count+1)
    else:
        return b, (a + b), count

fibonacci(1, 1, 0)

