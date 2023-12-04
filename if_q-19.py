'''
wap to accept three numbers from the user and
display the second largest
'''
num1 = int(input("Enter the 1st no.: "))
num2 = int(input("Enter the 2nd no.: "))
num3 = int(input("Enter the 3rd no.: "))

if (num1 > num2 and num2 > num3):
    print(f'{num1} is the largest no., \n \t{num2} is the second largest no.')
elif (num2 > num3 and num3 > num1):
    print(f'{num2} is the largest no., \n \t{num3} is the second largest no.')
else:
    print(f'{num3} is the largest no., \n \t{num1} is the second largest no.')