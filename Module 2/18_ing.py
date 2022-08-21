# 18. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' insteadif the string length of the given string is less than 3, leave it unchanged.

str_name = input("Enter String : ")
ing = 'ing'
ly = 'ly'
if str_name.isalpha():
  if len(str_name) >= 3:
    if str_name==ing:
      print(str_name+ly)
    else:
      str_name = str_name + ing
      print(str_name)
  else:
    print(str_name)
else:
  print("Please enter only String")