x=int(input())
y=[int(i) for i in input().split()]
max=b[0]
for j in range(0,x):
	if y[j]>max:
		max=y[j]
print(max)
