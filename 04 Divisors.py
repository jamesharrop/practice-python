'''
Divisors  - from practicepython.com
Exercise 4
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
'''

num = int(input("Enter a number: "))
print("Divisors are:")
divisors = [x for x in range(1, int(num/2)+1) if num%x == 0]
divisors.append(num)
print(divisors)