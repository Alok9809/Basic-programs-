#Write a function to check if a number is prime or not.
def prime(num):
    count = 0
    for i in range(1, num+1):
        if(num%i == 0):
            count += 1
    if(count == 2):
        return "Given no. is a prime no."
    else:
        return "Given no. is not a prime no."
    
num = int(input("Enter the number: "))
out = prime(num)
print(out)