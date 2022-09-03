# There are 3 types of variables in a python programming language.
# Instance variable.
# Local variable. X
# Static variable.

# 1. Instance Variable:

# The scope of the instance variable is inside the constructor. Also, data inside instance variable changes from object to object. This was the tough part and yes it might seem confusing.When you create a constructor inside the class, there are variables inside those constructors which is used to hold data coming directly from the object of a class.



class Darshan:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printing(self):
        print("My name is",self.name,"and Age is",self.age)


darshan = Darshan("Darshan",20)
darshan.printing()

# 2. Static variable.

# If the value of the variable does not change from object to object and if the variable is declared outside method and inside the class and also the value of variable remains same throughout this type of variable is called as static variable.


class Home:
    Name = "Darshan"
    Age = 20
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printing(self):
        print("My name is",self.name,"and age is",self.age)

home = Home("Ritik",21)
home.printing()
print("My name is",home.Name,"and age",home.Age)