# 17. Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.

q1 = input("Enter First String : ")
q2 = input("Enter Second String : ")

q3 = f'{q1} {q2}'
print(q3)

print("After Swap")
w1=' '.join(q1)
w2=w1.split()
w3=' '.join(q2)
w4=w3.split()

w2[0],w2[1]=w4[0],w4[1]

print(''.join(w2),''.join(w4))
# for i in range(0,2):
#   print(q1[i],end=" ")
#   print(q2[i],end=" ")
  