'''
Write a function to find factorial of a number but also store the
factorials calculated in a dictionary as done in the Fibonacci series.
'''

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact
while 1:
    dct = {}
    num = int(input("Enter the number: "))
    out = factorial(num)
    print(f'Factorial of a given number {num} if {out}')
    dct[num] = out
    print('Do you want to continue Y/N')
    if input() != 'Y':
        print(f'Your All Result {dct}')
        break
    
    
'''
Write a python function that received list of intergers and return 1 if all 
the integers values are sorted in ascending order and -1 if list is unsorted.
'''
