# 23. Write a Python function to insert a string in the middle of a string.

def func():
  string = "My name is darshan"
  print(string)
  lst = string.split()
  per = input("Where you want to insert: ")
  val = int(lst.index(per))+1
  user = input("Enter Subject: ")
  lst.insert(val,user)
  fnl = ' '.join(lst)
  print(fnl)

func()