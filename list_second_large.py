# second largest
n=int(input())
data=list(map(int,input().split()))
print(sorted(list(set(data)))[-2])
