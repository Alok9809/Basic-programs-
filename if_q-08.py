'''
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount
'''
bonus = 5/100
yos = int(input("Enter year of service: "))
salary = int(input("Enter your salary: "))

if (yos > 5):
    print(f'Bonus is {salary*bonus}')
else:
    print("No bonus")
