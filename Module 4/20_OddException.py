# Write python program that user to enter only odd numbers, else will raise an exception.

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
try:
    for i in numbers:
        print(i==i*2)
except Exception as ex:
    print(ex)