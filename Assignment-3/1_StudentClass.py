# Write a program to create a student class with name, age and marks as data members. Also create a method named display () to view the student details.Create an object to Student class and call the method using the object.

class Student:
    name = str()
    age = int()
    marks = int()
    def display(self,name,age,marks):
        print("Student Name is:",name)
        print("Age is:",age)
        print("Marks is:",marks)
    
darshan = Student()
darshan.display('Darshan',21,70)