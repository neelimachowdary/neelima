l=int(input())
temp=l
num=0
while l!=0:
	k=l%10
	l=l//10
	num += k**3
if num==temp:
	print("yes")
else:
	print("no")
