u=int(input())
v=[int(i) for i in input().split()]
min=v[0]
for j in range(0,u):
	if v[j]<min:
		min=v[j]
print(min)
