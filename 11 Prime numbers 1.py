''' Exercise 11 (and Solution)
Ask the user for a number and determine whether the number is prime or not.
The definition of a prime number is a positive integer that has exactly two positive divisors
'''

num = int(input("Enter a number: "))

def find_divisors(num):
    divisors = [x for x in range(1, int(num/2)+1) if num%x == 0]
    divisors.append(num)
    return divisors

def is_prime(num):
    return len(find_divisors(num)) == 2

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

def check_num_is_not_below_one(func):
    def inner(num):
        if num<1:
            print("Can't calculate that")
            return None
        return func(num)
    return inner

@check_num_is_not_below_one # A decorator is not the best way to structure this here
def is_prime_faster(num): # It stops looking once it finds any factor
    value = 1
    if num == 1:
        return False
    while True:
        value += 1
        if value > int(num ** 0.5):
            return(True)
        if num % value == 0:
            print(f'{int(num/value)} x {value} = {num}')
            return(False)

print("Try another method:")

if is_prime_faster(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")