#Write a function to calculate power of a number raised to other. E.g.- ab.
def power_raised(a, b):
    s = 1
    for i in range(b):
        s *= a
    return s
a = int(input("Enter the 1sr number: "))
b = int(input("Enter the 2nd number: "))
power = power_raised(a, b)

print(f'Power of a number raised to other is {power}')