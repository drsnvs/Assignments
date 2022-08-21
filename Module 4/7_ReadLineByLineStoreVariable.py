# 7. Write a Python program to read a file line by line store it into a variable.

file = open("NewFile.txt",'r')
# print(file.read())

for i in file.readlines():
    print("Line:",file.readline())