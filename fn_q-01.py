#  Write a function to calculate area and perimeter of a rectangle
def area_of_rect(l, b):
    return l*b
def peri_of_rect(l, b):
    return 2*(l+b) 
    
l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
area = area_of_rect(l, b)
peri = peri_of_rect(l, b)

print(f'Area of the Rectangle {area}')
print(f'Perimeter of the Rectangle {peri}')