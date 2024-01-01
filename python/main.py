from graphics import rectangle,circle
from graphics.threedgraphics import cuboid,sphere
#using rectangle module
l=int(input("Enter Length of the rectangle:"))
w=int(input("Enter width of the rectangle:"))
print("Area of rectangle=",rectangle.area(l,w))
print("Perimeter of rectangle=",rectangle.perimeter(l,w))
#using circle module
r=int(input("Enter the radius of the circle:"))
print("Area of circle=",circle.area(r))
print("Perimeter of circle=",circle.perimeter(r))
#using cuboid module
l1=int(input("Enter the length of the cuboid: "))
w1=int(input("Enter the width of the cuboid:"))
h1=int(input("Enter the height of the cuboid:"))
print("Surfacearea of cuboid=",cuboid.surface(l1,w1,h1))
print("Volume of cuboid=",cuboid.volume(l1,w1,h1))
#using sphere module
radius=int(input("Enter the radius of the sphere"))
print("Surfacearea of sphere=",sphere.surfacearea(radius))
print("Volume of sphere=",sphere.volume(radius))
