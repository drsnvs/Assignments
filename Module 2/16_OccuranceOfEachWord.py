# 16. Write a Python program to count the occurrences of each word in a given sentence

q1 = input("Enter three or four lines of string : ")
if q1.isprintable():
  q2 = input("Enter something in your string i'll tell you how many time occure a word : ")
  q3 = q1.count(q2)
  print(q3)
else:
  print("Enter a proper string")
