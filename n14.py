l=input()
b=input()
if l.isalpha() or b.isalpha():
    print("Invaild")
else:
    l=int(l)
    b=int(b)
    for i in range((l+1),b):
        if i%2!=0:
            print(i,end=' ')
