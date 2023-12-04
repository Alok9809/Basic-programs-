'''
Write a program to print absolute vlaue of a number entered by user. E.g.-
INPUT: 1        OUTPUT: 1
INPUT: -1        OUTPUT: 1
'''
num = int(input("Enter the no.: "))
if (num < 0):
    print(f'|{num}| = {-1*num}')
else:
    print(f'|{num}| = {num}')