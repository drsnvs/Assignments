# Write a program to generate prime numbers with the help of a function to test prime or not.
number = int(input("Enter Number: "))
for i in range(2,number):
    if (number%2)==0:
        print("Not Prime")
        break
    else:
        print("Prime")
        break