# 9. Write a Python program to count the number of lines in a text file.

file = open("NewFile.txt","r+")
description = '''Helllo Everyone.
This is GitHub.
I am writting a code in it.
I am using Visualstudio code editor.'''
file.write(description)
file.seek(0)
print("Length is:",len(file.readlines()))
file.close()