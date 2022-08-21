# 21. Write a Python function to reverses a string if its length is a multiple of 4

inpt = input("Enter A String: ")
inpt_len = len(inpt)
if inpt_len%4==0:
    print(inpt[::-1])
else:
    print(inpt)