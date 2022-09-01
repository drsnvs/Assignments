# Create a dictionary that will accept cricket players name and scores in a match. Also, we are retrieving runs by entering the player’s name.

name = input("Enter Your Name: ")
score = int(input("Enter Your Score: "))

cricket = dict()

cricket.setdefault('Name',name)
cricket.setdefault('Score',score)

search = input("Enter Name for search your scores: ")
if cricket["Name"]==search:
    for i in cricket:
        print(i,end='\t')
    print()
    for i in cricket.values():
        print(i,end='\t')
else:
    print("Enter Valid Name Please")