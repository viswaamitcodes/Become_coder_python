n=int(input())
data=list(map(int,input().split()))
c=0
lis=[]
for i in data:
    if i==1:
        c+=1
        lis.append(c)
    if i!=1:
        c=0
print(max(lis))