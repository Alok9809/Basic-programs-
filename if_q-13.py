'''
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
'''

a = int(input("Enter the no. of classes held: "))
b = int(input("Enter the no. of classes attended: "))
percentage = (b/a)*100
print(f'Your attendence is {percentage}%')
if (percentage > 75):
    print("\n \t You are allowed to sit in examination hall")
else:
    print("\n \t You are not allowed to sit in examination hall")