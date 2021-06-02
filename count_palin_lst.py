def lst_pal(n,data):
    count=0
    num=0
    for i in data:
        j=i
        while j:
            r=j%10
            j//=10
            num=num*10+r
        if num==i:
            count+=1
        num=0
    return count
n=int(input())
data=list(map(int,input().split()))
print(lst_pal(n,data))
    
        

