#Write a Python program to create a class that represents a shape. Include methods to calculate
#its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

import math

class Shape():
    global circle,rectangle,triangle,square
    def __init__(self,shape):
         self.shape = shape
         
    def shapeSelect(self,shape):
        if (self.shape==1):
            radius=float(input('enter the radius of your circle : '))
            circle(self,radius)
        if self.shape == 2:
            length =float(input('enter the length of your rectangle : '))
            width =float(input('enter the width of your rectangle : '))
            rectangle(self,length,width)

        if self.shape == 3:
            base =float(input('enter the base of your triangle : '))
            height =float(input('enter the height of your triangle : '))
            side1 =float(input('enter the side1(hypotenuse1) of your triangle : '))
            side2 =float(input('enter the side2(hypotenuse2) of your triangle : '))
            triangle(self,base,height,side1,side2)

        if self.shape == 4:
            side =float(input('enter the length of your square : '))
            square(self,length,width)


    def circle(self,radius):
        area=math.pi*radius*radius
        perimeter=2*math.pi*radius
        print( area,perimeter)

    def rectangle(self,length,width):
        area=length*width
        perimeter=2*(length+width)
        print( area,perimeter)

    def triangle(self,base,height,side1,side2):
        area=0.5*base*height
        perimeter=base+side1+side2
        print( area,perimeter)

    def square(self,side):
        area=side*side
        perimeter=4*side
        print( area,perimeter)


print('a program that computes area and perimeter of different shapes')
shapes=['1. circle','2. Rectangle','3. Triangle', '4. square']
print(shapes)
shape=int(input('select the shape of your liking : '))
item=Shape(shape) #place the variables in init function
item.shapeSelect(shape)  
