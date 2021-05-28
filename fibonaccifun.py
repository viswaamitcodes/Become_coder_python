def fib_fun(n,m):
    a,b=0,1
    c=0
    for i in range(m):
        if a>=n and a<=m:
            print(a,end=" ")
        if a>m:
            return
        c=a+b
        a=b
        b=c  
n,m=map(int,input().split())   
fib_fun(n,m)
