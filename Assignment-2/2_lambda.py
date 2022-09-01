# Write a lambda/Anonymous function to find bigger number in two given numbers.

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
lmd = lambda num1,num2 : max(num1,num2)

print("Max is:",lmd(num1,num2))