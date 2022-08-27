# 27. The isinstance() function checks if the object (first argument) is an instance or subclass of the class info class (second argument).


name = 'Darshan'
print(isinstance(name,int)) # False
print(isinstance(name,str)) # True


class Animal:
    def __init__(self,name):
        self.name = name
obj = Animal('Darshan')

print(isinstance(obj,Animal)) # True