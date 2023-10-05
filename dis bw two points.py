#input section

x1 = int(input("enter the x1 coordinate "))

y1 = int(input("enter the y1 coordinate"))

x2 = int(input("eneter the x1 coordinate"))

y2 = int(input("enter the y2 coordinate"))

#logic section

s = ((y2 - y1)**2 + (x2 - x1)**2)**0.5

#dispay section

print("the distance between two points is" , s)
