# 11. Write a python program to sum of the first n positive integers.

q = input("Enter Number : ")
k=int(q)
u=0
for i in range(1,k+1):
  u = i+u
print(u)