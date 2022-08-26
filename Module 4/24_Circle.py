# 24. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

# area = π r²
# perimeter = 2*r*3.14

class Circle:
    def areaOfCircle(self,radius):
        return 3.14*radius*radius
    def perimeterOfCircle(self,radius):
        return 2*radius*3.14

Obj = Circle()
print("Area of Circle is:",Obj.areaOfCircle(12.5))
print("Perimeter Of Circle is:",Obj.perimeterOfCircle(17.8))