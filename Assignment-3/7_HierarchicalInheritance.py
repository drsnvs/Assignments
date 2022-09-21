# Write a program to implement hierarchical inheritance.


class Parents():
    def Bike(self):
        print("Bike From Parent.")
    def Scooty(self):
        print("Scooty From Parent.")
    def Jewlarry(self):
        print("Jewlarry From Parent.")
    def Business(self):
        print("Business From Parent.")

class Child1(Parents):
    def Class_12(self):
        print("Child 1 in class 12.")

class Child2(Parents):
    def Class_10(self):
        print("Child 2 in class 10.")

brother = Child1()
sister = Child2()

brother.Class_12()
brother.Bike()
brother.Business()

sister.Class_10()
sister.Scooty()
sister.Jewlarry()