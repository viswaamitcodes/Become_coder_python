n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2==0:
            j=0
            print(j,end="")
        else:
            j=1
            print(j,end="")
    print()
         