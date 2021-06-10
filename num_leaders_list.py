n=int(input())
data=list(map(int,input().split()))
def leaders(n,data):
    for i in range(n):
        if data[i]==max(data[i:]):
            print(data[i],end=" ")
    print()
leaders(n,data)
