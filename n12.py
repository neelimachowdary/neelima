m=int(input())
u=m
rev=0
while(m>0):
    x=m%10
    rev=rev*10+x
    m=m//10
if(u==rev):
    print("yes")
else:
    print("no")
