# 23. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def areaOfRecatangle(self):
        areaOfRec = self.length * self.width
        return areaOfRec

Area = Rectangle(10,15)
print("Area Of Rectangle is:",Area.areaOfRecatangle())