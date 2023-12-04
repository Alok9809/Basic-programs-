''' 
wap to accept the cost price of a bike and dislay the road tax
to be paid according to the following criteria:

cost price(in Rs)                     Tax
> 100000                              15%
> 50000 and <= 100000                 10%
<= 50000                              5%
'''
tax = 0
cp = int(input("Enter the cost price of bike: "))
if (cp <= 50000):
    tax = tax + 5/100*cp
elif (50000 < cp <= 100000):
    tax =  tax + 10/100*cp
else:
    tax = tax + 15/100*cp 
print(f'Tax to be paid {tax}')