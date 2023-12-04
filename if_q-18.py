'''
wap to accept three sides of a triangle and check whether it is an
equilateral, isosceles or scalene triangle 
'''

a = int(input("Enter the 1st side of a traiangle: "))
b = int(input("Enter the 2nd side of a traiangle: "))
c = int(input("Enter the 3rd side of a traiangle: "))
triangle = (f'In triangle, PQR a = {a}, b = {b} and c = {c}')
print(triangle)
if (a == b == c):
    print("\t Therefore, triangle PQR is a equilateral triangle")
elif (a != b != c):
    print("\t Therefore, triangle PQR is a scalene triangle")
elif (a == b or b == c or a == c):
    print("\t Therefore, triangle PQR is a isosceles triangle")