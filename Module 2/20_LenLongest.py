# 20. Write a Python function that takes a list of words and returns the length of the longest one.
lst = list()
lst = ["Gujarat","University","College"]
lst2 = list()
for i in lst:  
  num = len(i)
  lst2.append(num)
print(max(lst2))