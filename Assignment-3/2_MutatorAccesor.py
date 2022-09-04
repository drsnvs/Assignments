# Write a program to store data into instances using mutator methods and to retrieve data from the instances using accessor methods.

class Car:
    def __init__(self,name):
        self.carname = name
    def accessor(self,carname):
        self.carname = carname
    def mutator(self):
        return self.carname

first = Car('Scorpio')
print(first.mutator())

first.accessor('Ferarri')
print(first.mutator())