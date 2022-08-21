# 3. Write a Python program to get the Fibonacci series of given range. *****************
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,

# 0,1,2,3,4,5,6,7,8,9
a=0
b=1
for i in range(0,10):
  d = a + b # 0 + 1
  b = a # 0
  a = d # 1
  print(a)

# 2nd Example:

a = 0
b = 1
inn = int(input("Enter Number : "))
for i in range(0,inn):
  c = a + b
# 0 = 0 + 1
  b = a
# 1 = 0
  a = c
# 0 = 1
  print(c)