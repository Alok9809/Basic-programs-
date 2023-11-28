def area_of_rect(l,b):
    return l*b
def perimeter_of_rect(l,b):
    return 2*(l+b)

length = int(input('enter the length'))
breadth = int(input('enter the breadth'))
area = area_of_rect(length,breadth)
perimeter = perimeter_of_rect(length,breadth)

print(f'area of rectangle{area}')
print(f'perimeter of rectangle{perimeter}')
    
