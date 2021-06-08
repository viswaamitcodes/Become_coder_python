n=int(input())
high=0
low=0
c=0
data=list(map(int,input().split()))
for i in range(n-1):
    if data[i]==data[i+1]:
        c+=1
    if data[i]<=data[i+1]:
        low+=1
    if data[i]>=data[i+1]:
        high+=1
if (high==n//2-1 and low==n//2) or (low==n//2-1 and high==n//2) or (high==low and c==0):
    print(True)
else:
    print(False) 