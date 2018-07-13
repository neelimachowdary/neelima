u=int(input())
v=input()
v=[int(i) for i in v.split()]
v.sort()
for i in range (0,u):
    print(v[i],end=" ")
