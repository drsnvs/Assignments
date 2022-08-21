# 15. Write a Python program to count occurrences of a substring in a string.

w1 = input("Enter Anything : ")
w2 = input("Enter something in on your string : ")
if w1.isprintable():
  w3 = w1.split()
  # for i in range(0,len(w3)):
  if w2 in w3:
    w4=w3.count(w2)
    print(w4)
    # break
  else:
    print("Not found here")
    # break
else:
  print("Not found")
