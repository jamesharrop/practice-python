''' 
Sieve_of_Eratosthenes
Find low value primes quickly
'''

def sieve(num): 
    A = [True] * num
    for i in range(2, int(num ** 0.5)):
        if A[i]:
            for j in range(i**2, num-1, i):
                A[j] = False
    output = []
    for n in range(2,num):
        if A[n]:
            output.append(n)
    return output


print(sieve(5000))