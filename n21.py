n=int(input())
r=int(input())
d=int(input())
sum=0
while n!=0:
	sum=sum+r
	r=r+d
	n=n-1
print(sum)
