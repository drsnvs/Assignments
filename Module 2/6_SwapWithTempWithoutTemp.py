# 6. Write python program that swap two number with temp variable and without temp variable.

# with use of temp
print("With Temp")
x=1
y=2
print("before")
print(x)
print(y)
print("after")
temp = x
x = y
y = temp
print(x)
print(y)

# without temp
print("\nWithout temp")
a=3
b=5
print("Before")
print(a)
print(b)
a,b=b,a
print("After")
print(a)
print(b)