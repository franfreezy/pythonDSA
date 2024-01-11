#Write a Python program to create a class that represents a shape. Include methods to calculate
#its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

import math

class Shape():
    global circle,rectangle,triangle,square
    def __init__(self,shape):
         self.shape = shape
         
    def shapeSelect(self,shape):
        if (self.shape==0):
            radius=float(input('enter the radius of your circle : '))
            circle(self,radius)
        if self.shape == 1:
            length =float(input('enter the length of your rectangle : '))
            width =float(input('enter the width of your rectangle : '))
            rectangle(self,length,width)

        if self.shape == 2:
            base =float(input('enter the base of your triangle : '))
            height =float(input('enter the height of your triangle : '))
            side1 =float(input('enter the side1(hypotenuse1) of your triangle : '))
            side2 =float(input('enter the side2(hypotenuse2) of your triangle : '))
            triangle(self,base,height,side1,side2)

        if self.shape == 3:
            side =float(input('enter the length of your square : '))
            square(self,length,width)


    def circle(self,radius):
        area=math.pi*radius*radius
        perimeter=2*math.pi*radius
        print('area of '+ shapes[shape] +' with radius '+ str(radius)+ ' is : '+ str(area)+ ' and its perimeter is : '+ str(perimeter))

    def rectangle(self,length,width):
        area=length*width
        perimeter=2*(length+width)
        print('area of '+ shapes[shape] + ' with length :'+ str(length)+' and width :'+str(width) +' is : '+ str(area)+ ' and its perimeter is : '+ str(perimeter))


    def triangle(self,base,height,side1,side2):
        area=0.5*base*height
        perimeter=base+side1+side2
        print('area of '+ shapes[shape] +' with base :'+ str(base)+' and height :'+str(height) +' is : '+ str(area)+ ' and its perimeter is : '+ str(perimeter))


    def square(self,side):
        area=side*side
        perimeter=4*side
        print('area of '+ shapes[shape] +' with side :'+ str(side)+' is : '+ str(area)+ ' and its perimeter is : '+ str(perimeter))



print('a program that computes area and perimeter of different shapes')
shapes=[' circle','Rectangle','Triangle', ' square']
print(shapes)
print('enter 0 to 4 for respective shape ')
shape=int(input('select the shape of your liking : '))
item=Shape(shape) #place the variables in init function
item.shapeSelect(shape)  
