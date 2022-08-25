# 12. Write a Python program to copy the contents of a file to another file.

file = open("NewFile.txt","r+")
description = '''Helllo Everyone.
This is GitHub.
I am writting a code in it.
I am using Visualstudio code editor.'''
file.write(description)
file.seek(0)
data = file.read()
clone = open("NewFileCopy.txt",'w')
clone.write(data)
file.close()
clone.close()