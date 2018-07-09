L=input()
M=input()
s=0
if L.isalpha() or M.isalpha():
    print("Invalid")
else:
    L=int(L)
    M=int(M)
    arr=[int(input()) for _ in range(L)]
    for i in range(M):
        s=s+arr[i]
    print(sum)
