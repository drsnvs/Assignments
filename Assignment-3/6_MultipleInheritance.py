# Write a program to implement multiple inheritance using two base classes.

class Father:
    def House(self):
        print("This is House from Father.")
    def Bussiness(self):
        print("This is Bussiness from Father.")

class Mother:
    def Money(self):
        print("This is Money from Mother.")
    def Blessings(self):
        print("This is Blessings from Mother.")

class Child(Father,Mother):
    def Toys(self):
        print("This is Toys from Child.")

darshan = Child()
darshan.House()
darshan.Bussiness()
darshan.Money()
darshan.Blessings()
darshan.Toys()