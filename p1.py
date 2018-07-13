def reverse(k):
  str = ""
  for j in k:
    str = j + str
  return str
 
k = input()
print (reverse(k))
