def prime(x):
    count = 0
    for i in range (1,x+1):
        if x%i==0:
            count+=1
    return count == 2
num = 7
out = prime(num)
print(out)
