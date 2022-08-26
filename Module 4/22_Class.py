# 22. How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

# With class keyword we can define a class.

# self is point to the object.

# Example:

class House:
    def parts(self):
        parts = ["Fan","Table","Locker","Dining-Table"]
        print("This is Computer class")
        for i in parts:
            print("Computer Parts : ",i)

obj = House()
obj.parts()