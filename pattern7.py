n=int(input())
c=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if c==0:
            print(c,end="")
            c=1
        else:
            print(c,end="")
            c=0
    print()
         