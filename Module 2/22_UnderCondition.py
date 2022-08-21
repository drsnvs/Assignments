# 22. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length islessthan 2,return instead of the empty string.
# o Sample String:w3resource'
# o Expected Result: 'w3ce'
# o Sample String: 'w3'
# o Expected Result: 'w3w3'
# o Sample String: ' w'
# o Expected Result: Empty String

inpt = input("Enter a String: ")
if inpt[0] == ' ':
    print("Empty String")
elif len(inpt)>2:
    two_str = inpt[0:2] + inpt[len(inpt)-2:len(inpt):1]
    print(two_str)
elif len(inpt)<=2 and len(inpt)>0:
    second = inpt[0:2] + inpt[0:2]
    print(second)
else:
    print("Enter a Valid String.")