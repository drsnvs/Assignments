# 12. Write a Python program to calculate the length of a string.

g = input("Enter Anything for length of your string : ")
if g.isalpha():
  print(len(g))
else:
  print("Enter String only")