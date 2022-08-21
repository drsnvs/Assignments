# 6. Write a Python program to read a file line by line and store it into a list

file = open("NewFile.txt",'r')
split_file=file.read().splitlines()
print(split_file)