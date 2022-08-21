# 8. Write a python program to find the longest words.

file = open("NewFile.txt","r+")
description = '''Helllo Everyone.
This is GitHub.
I am writting a code in it.
I am using Visualstudio code editor.'''
file.write(description)
file.seek(0)
reading = file.read().split()
print(max(reading,key=len))
file.close()
