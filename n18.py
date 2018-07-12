o,y=input().split()
o=int(o)
y=int(y)
for a in range(o,y):
	temp=a
	num=0
	while a!=0:
		b=a%10
		a=a//10
		num += b**3
	if num==temp:
		print(temp,end=" ")
