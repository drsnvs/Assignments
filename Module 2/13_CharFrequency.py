# 13. Write a Python program to count the number of characters (character frequency) in a string

t = input("Enter String Only : ")
k=0
if t.isalpha():
  for i in range(0,(len(t))):
    k=i+1
  for i in range(0,(len(t))):
    a4 = f"{k}"
    a1=f"{i}"
    a2=f"{i+1}".zfill(len(a4))
    a3=f"{a2} index : {t[i]}"
    print(a3)
    # print(i+1,"index :",t[i])
  print(t,": Length is =",k)
else:
  print("Enter Only string Please")