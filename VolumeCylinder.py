import math

radius = int(input("The radius of the circle is: "))
height = int(input("The height of the cylinder is: "))

radiussqr = radius * radius
area = 3.14 * radiussqr
volume = area * height

print("The volume of the cylinder is ", round(volume,1))