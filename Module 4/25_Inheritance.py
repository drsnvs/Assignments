# 25. Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

# Inheritance relationship defines the classes that inherit from other classes as derived, subclass, or sub-type classes. Base class remains to be the source from which a subclass inherits. For example, you have a Base class of “Animal,” and a “Lion” is a Derived class. The inheritance will be Lion is an Animal

# Benefits of inheritance are: 
# 1. It represents real-world relationships well.
# 2. It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
# 3. It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

# "__init__" is a reserved method in python classes. It is known as a constructor in OOP concepts. This method called when an object is created from the class and it allows the class to initialize the attributes of a class.

# Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.

class Animal:
    pass

class Lion(Animal):
    def __init__(self,name):
        self.name = name
        print("This is Animal Class by init.")

    def roar(self):
        print("A",self.name,"can Roar.")

lion_obj = Lion("Lion")
lion_obj.roar()