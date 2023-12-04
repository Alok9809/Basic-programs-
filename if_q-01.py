# calculating the electric bill with the help unit given by user
# unit                   price
# First 100 units        no charge
# Next 100 units         Rs 5 per Unit 
# After 200 units        Rs 10 per unit   

amt = 0
nu = int(input("Enter the no. of units = "))
if(0<nu<=100):
    amt = 0
if(100<nu<=200):
    amt = (nu-100)*5
if(nu>200):
    amt = (nu-200)*10+500
print(f'Your Electric Bill is {amt}')