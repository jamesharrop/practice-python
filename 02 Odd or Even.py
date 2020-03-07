'''
2
Check if a number is odd or even
'''

def odd_or_even_using_modulus(n):
    if n%2 == 0:
        return("Even")
    else:
        return("Odd")

def odd_or_even_using_bitwise_and(n):
    if n&1 == 0:
        return("Even")
    else:
        return("Odd")

if __name__ == "__main__":    
    n = int(input("Number? "))
    print(odd_or_even_using_modulus(n))
    print(odd_or_even_using_bitwise_and(n))