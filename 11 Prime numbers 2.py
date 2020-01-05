''' 
Make a list of prime numbers
'''

def is_prime_faster(num): 
    value = 1
    if num < 1:
        raise ValueError
    if num == 1: # 1 is not a prime number as it does not have 2 different factors
        return False
    while True:
        value += 1
        if value > int(num ** 0.5):
            return(True)
        if num % value == 0:
            print(f'{int(num/value)} x {value} = {num}')
            return(False)

for n in range(2, 500):
     if is_prime_faster(n):
         print(f'{n} is Prime')

