# import necessary libraries
import numpy as np

class GeomentryShape: # define the class of Shapes
    def __init__(self, type='', r=1, h=1, w=1, a=1, b=1, c=1): # define and set the default values
        self.type = type
        if r <= 0 or h <= 0 or w <= 0 or a <= 0 or b <= 0 or c <= 0 or type not in ['circle', 'rectangle', 'triangle']: # check if the input is valid
            print('Invalid input: Not support shape or the input is invalid')
            exit(1)
        elif self.type == 'circle':
            self.r = r
        elif self.type == 'rectangle':
            self.h = h
            self.w = w
        elif self.type == 'triangle':
            if a + b <= c or a + c <= b or b + c <= a: # check if the input is valid
                print('Invalid input: illegal triangle sides')
                exit(1)
            self.a = a
            self.b = b
            self.c = c
    
    # calculate the area
    def Area(self):
        if self.type == 'circle':
            return np.pi * self.r ** 2 # circle area
        elif self.type == 'rectangle':
            return self.h * self.w # rectangle area 
        elif self.type == 'triangle':
            s = (self.a + self.b + self.c) / 2 # Heron's formula for triangle area
            return np.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) 
    
    # calculate the perimeter
    def Perimeter(self):
        if self.type == 'circle':
            return 2 * np.pi * self.r # circle perimeter
        elif self.type == 'rectangle':
            return 2 * (self.h + self.w) # rectangle perimeter
        elif self.type == 'triangle':
            return self.a + self.b + self.c # triangle perimeter
    
    # display the shape information
    def Display(self):
        if self.type == 'circle':
            print(f'Circle: radius = {self.r}, area = {self.Area()}, perimeter = {self.Perimeter()}')
        elif self.type == 'rectangle':
            print(f'Rectangle: height = {self.h}, width = {self.w}, area = {self.Area()}, perimeter = {self.Perimeter()}')
        elif self.type == 'triangle':
            print(f'Triangle: side1 = {self.a}, side2 = {self.b}, side3 = {self.c}, area = {self.Area()}, perimeter = {self.Perimeter()}')

# test
circle = GeomentryShape('circle', r=3)
circle.Display()
rectangle = GeomentryShape('rectangle', h=22, w=3)
rectangle.Display()
triangle = GeomentryShape('triangle', a=3, b=4, c=5)
triangle.Display()
exit()