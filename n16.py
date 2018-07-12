a,b=input().split()
a=int(a)
b=int(b)
for m in range(a+1,b):
	cnt=0
	for i in range(1,c+1):
		if m%i==0:
			cnt=cnt+1
	if cnt==2:
		print (m,end=" ")
