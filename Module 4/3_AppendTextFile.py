# 3. Write a Python program to append text to a file and display the text.

file = open("NewFile.txt","a+")
file.seek(0)
file.write("\nI am learnig Python Language")
file.seek(0)
print(file.read())
file.close()