# Write a program to override super class constructor and method in sub class.

class Laptop:
    def __init__(self,Parameter):
        self.Parameter = Parameter
        print("This is Laptop",Parameter)
    def display(self):
        print("This is a Display of Laptop")

class Computer(Laptop):
    def __init__(self,Parameter):
        self.Parameter = Parameter
        print("This is Computer",Parameter)
    def display(self):
        print("This is a Display of Computer")
    def override(self):
        super().__init__('Darshan')
        super().display()

cp = Computer('Darshan VS')
cp.display()
cp.override()