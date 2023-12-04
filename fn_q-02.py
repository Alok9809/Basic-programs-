# Write a function to calculate area and circumference of a circle.
def area_of_circle(r):
    return 3.14*r*r
def circum_of_circle(r):
    return 2*3.14*r 
    
r = int(input("Enter the radius: "))
area = area_of_circle(r)
circum = circum_of_circle(r)

print(f'Area of the Circle {area}')
print(f'Circumference of the Circle {circum}')