def even_or_not(num):
    if num%2 == 0:
        return "number is even"
    else:
        return "number is odd"

num = int(input("enter the number"))
out = even_or_not(num)
print(out)
