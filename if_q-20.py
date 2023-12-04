'''
wap to accept the kilometers covered and calculate the
bill according to the following criteria

first 10 km               rs 11/km
next 90 km                rs 10/km
after that                rs 9/km
'''

km = int(input("Enter the kilometers covered: "))

if (0 < km <= 10):
    bill = km * 11
elif (10 < km <= 100):
    bill = 110 + ((km-10) * 10)
elif (km > 100):
    bill = 1010 + (km - 100)*9
print(f'Total amount to pay is {bill}')