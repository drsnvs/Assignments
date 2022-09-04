# Create a student class to with the methods set_id, get_id, set_name, get_name,set_marks and get_marks where the method name starting with set are used to assign the values and method name starting with get are returning the values.Save the program by student.py. Create another program to use the student class which is already available in student.py.


class Student:
    def __init__(self):
        id = int()
        name = str()
        marks = int()
        self.id = id
        self.name = name
        self.marks = marks
    def set_id(self):
        self.id = int(input("Enter Your Id: "))
    def get_id(self):
        return self.id
    def set_name(self):
        self.name = input("Enter Your Name: ")
    def get_name(self):
        return self.name
    def set_marks(self):
        self.marks = int(input("Enter Your Marks: "))
    def get_marks(self):
        return self.marks

