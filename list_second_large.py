# second largest
n=int(input())
data=list(map(int,input().split()))
data.sort()
print(data[-2])