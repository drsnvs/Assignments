# 19. Write a Python program to find the first appearance of the substring 'not' and 'poor' froma given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'substring with 'good'. Return the resulting string.
sub_str = input("Enter String : ")
spt = sub_str.split()
print("You Entered:",sub_str)
if 'not' and 'poor' in sub_str:
  spt.remove('not')
  spt.remove('poor')
  print(' '.join(spt))