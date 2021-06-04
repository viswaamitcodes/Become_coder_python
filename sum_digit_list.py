def sum(n,data):
    digitsum=0
    numlist=0
    for i in data:
        for j in str(i):
            digitsum+=int(j)
        numlist.append(digitsum)
        digitsum=0
n=int(input())
data=list(map(int,input().split()))
sum(n,data)
print(*data)