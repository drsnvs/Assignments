# Write a program to access the base class constructor from a sub class by using super () method and also without using super () method.

class Parent:
    def __init__(self):
        print("This is Parent")

class Child(Parent):
    def __init__(self):
        print("This is Child")
    def super_method(self):
        super().__init__()

class Child2(Parent):
    def __init__(self):
        print("This is Child 2")
    def without_super_method(self):
        obj = Parent()
child = Child()
child.super_method()
child2 = Child2()
child2.without_super_method()