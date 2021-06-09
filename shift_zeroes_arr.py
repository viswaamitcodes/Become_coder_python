n=int(input())
data=list(map(int,input().split()))
def movezeroes(n,data):
    lis=data.copy()
    c=0
    for i in data:
        lis.remove(0)
        lis.append(0)
    print(*lis)
movezeroes(n,data)