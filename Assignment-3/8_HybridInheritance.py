# Write a program to implement hybrid inheritance.

class GrandParent:
    def Blessings(self,name):
        print("Blessings From Grand Parents to",name)

class Father(GrandParent):
    def Bike(self,name):
        print("Bike From Father to",name)

class Mother(GrandParent):
    def Scooty(self,name):
        print("Scooty From Mother to",name)



class Child1(Father,Mother):
    def Fisrt_child(self,name):
        print("First Child Name is:",name)

class Child2(Father,Mother):
    def Second_child(self,name):
        print("Second Child Name is:",name)

class Business(Child1,Child2):
    def Steel(self):
        print("Steel Business From Children")

name = "Darshan"
brother = Child1()
brother.Fisrt_child(name)
brother.Blessings(name)
brother.Bike(name)
print()
name = "Darshana"
sister = Child2()
sister.Second_child(name)
sister.Blessings(name)
sister.Scooty(name)
print()
business = Business()
business.Steel()