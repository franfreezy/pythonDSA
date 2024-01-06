#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
#ex1 on object oriented programming
import math
print(' A program that utilises OOP to calculate area and perimeter')

radius=float(input('Enter the radius of your circle:  '))

class Circle():
    # we use te init def to start, 
    def __init__(self, radius):
        self.radius=radius

    def Area(self):
        area = math.pi * self.radius * self.radius
        return area

    def Perimeter(self):
        perimeter=2 * math.pi * self.radius
        return perimeter


#we now create an object of a given circle- a specific circle, or this particular circle
circle = Circle(radius)

Area= circle.Area()
Perimeter=circle.Perimeter()
print('Area of a circle with radius '+str(radius)+' is : ' + str(Area))
print('Perimeter of a circle with radius '+str(radius)+' is : ' + str(P))





