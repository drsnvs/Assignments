# 5. Write a Python program to read last n lines of a file.

file = open("NewFile.txt",'r')
splitt = file.read().splitlines()
print(splitt[len(splitt)-1])
file.close()