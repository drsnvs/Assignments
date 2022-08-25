# 10. Write a Python program to count the frequency of words in a file.
from collections import Counter

file = open("NewFile.txt","r+")
description = '''Helllo Everyone.
This is GitHub.
I am writting a code in it.
I am using Visualstudio code editor.'''
file.write(description)
file.seek(0)

print(Counter(file.read().split()))

file.close()