g=int(input())
h=int(input())
i=int(input())
if(g>h) and (g>i):
    largest=g
elif(h>g) and (h>i):
    largest=h
else:
    largest=i
print(largest)
