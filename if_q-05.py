# wap to check whether the  last digit of a given no. is divisible by 3 or not.

digit = int(input("Enter the digits = "))
n = digit % 10
if(n % 3 == 0):
    print(f'Last digit of {digit} is divisible by 3')
else:
    print(f'Last digit of {digit} is not divisible by 3')
