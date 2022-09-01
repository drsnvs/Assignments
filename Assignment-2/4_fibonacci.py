# Write a program to generate Fibonacci series using user defined function.

number = int(input("Enter Number: "))
def fibonacci(number):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,number):
        c = a + b
        a = b
        b = c
        print(c)
        
fibonacci(number)