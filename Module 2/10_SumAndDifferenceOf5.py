# 10. Write a Python program that will return true ifthe two given integervalues are equal or their sum or difference is 5

a = int(input("Enter Number 1 : "))
b = int(input("Enter Number 2 : "))

sum = a+b
dif = a-b
ans =5
if a==b:
  print("Equal")
elif sum==5:
  print("Sum is True ")
elif dif==5:
  print("Difference is True, "+ans)
else:
  print("Not Valid")