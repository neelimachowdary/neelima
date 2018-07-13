import statistics
m=int(input())
n=input()
n=[int(i) for i in n.split()]
x=statistics.median(n)
print(x)
