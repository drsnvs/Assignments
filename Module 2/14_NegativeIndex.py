# 14. What are negative indexes and why are they used?

# As we know, indexes are used in arrays in all the programming languages. We can access the elements of an array by going through their indexes. But no programming language allows us to use a negative index value such as -4. Python programming language supports negative indexing of arrays, something which is not available in arrays in most other programming languages. This means that the index value of -1 gives the last element, and -2 gives the second last element of an array. The negative indexing starts from where the array ends. This means that the last element of the array is the first element in the negative indexing which is -1.

# index ____0___1___2___3___4___5__
# list1 = ['a','b','c','d','e','f']
# index ___-6__-5__-4__-3__-2__-1__

# Example:1

# Example

list1 = ['a','b','c','d','e','f']

print(list1)
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])
print(list1[-1])
print(list1[-2])
print(list1[-3])
print(list1[-4])
print(list1[-5])
print(list1[-6])

# Example:2

list2 = ['a','b','c','d','e']
for i in range(0,len(list2)):
  print(i,'\t',list2[i])
for i in range(0,-(len(list2)+1),-1):
  print(i,'\t',list2[i])