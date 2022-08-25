# 11. Write a Python program to write a list to a file.

file = open("NewFile.txt","w")
description = '''Helllo Everyone.
This is GitHub.
I am writting a code in it.
I am using Visualstudio code editor.'''.split()
file.write(' '.join(description))

file.close()