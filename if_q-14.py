# wap to check whether an years is leep year or not.

yr = int(input("Enter the year: "))
if (yr % 100 == 0):
    if (yr % 400 == 0):
        print(f'{yr} is a leap year')
    else:
        print(f'{yr} is not a leap year')
else:
    if (yr % 4 == 0):
        print(f'{yr} is a leap year')
    else:
        print(f'{yr} is not a leap year')