import array as arr

numbers = arr.array('i',[1,2,3,4,5,6,7,8,9,10])
print(numbers)
for i in numbers:
    print(i,end = ' ')
print()

numbers_bytes = bytes(numbers)
print(numbers_bytes)