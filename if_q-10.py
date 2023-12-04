'''
Take two int values from user and print greatest among them.
'''

a = int(input("Enter the 1st no.: "))
b = int(input("Enter the 2nd no.: "))
if (a > b):
    print(f'{a} is gratest among {a,b} ')
elif(b > a):
    print(f'{b} is greatest among {a,b}')
else:
    print('Both are equals')