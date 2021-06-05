n=int(input())
data=list(map(int,input().split()))
def leastrepeatedval(n,data):
    li1=[]
    li3=[]
    for i in data:
       li1.append(data.count(i))
    num=min(li1)
    for i in data:
        if data.count(i)==num:
            if i not in li3:
                li3.append(i)
    return li3
print(*leastrepeatedval(n,data))