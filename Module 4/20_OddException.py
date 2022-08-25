# 20. Write python program that user to enter only odd numbers, else will raise an exception.

# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
try: 
    num = int(input("Enter Number: "))
    if num%2==0:

        raise NameError("Odd Only")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not