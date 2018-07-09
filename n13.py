u=int(input())
v=u
count=0
while v!=0:
	if u%v==0:
		count=count+1
	v=v-1
if count==2:
	print("yes")
else:
	print("no")
