# 9. Write a Python program to sum of three given integers.However, if two values are equal sum will be zero.

# num1 = input("Enter Number 1 : ")
# num2 = input("Enter Number 2 : ")
# num3 = input("Enter Number 3 : ")

num1 = int(input("Enter 1 : "))
num2 = int(input("Enter 2 : "))
num3 = int(input("Enter 3 : "))

if num1 is num2 or num2 is num3 or num3 is num1:
  print(0)
else:
  ans = num1+num2+num3
  print(ans)