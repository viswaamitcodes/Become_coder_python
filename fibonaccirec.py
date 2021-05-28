def fibonacci(a,b,n):
    if b<n:
        print(a,end=" ")
        c=a+b
        fibonacci(b,c,n)
fibonacci(0,1,3)

    