'''
wap that accept the temperature in degree celsius of water
and check whether it is boiling or not
(boiling point of water in 100 degree celcius)
'''

t = int(input("Enter the temperature(degree celsius): "))
if (t >= 100):
    print('Water is boiling')
else:
    print('Water is not boiling')