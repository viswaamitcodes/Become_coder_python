def maxno(n,data):
    max=data[0]
    for i in range(n):
        if max<data[i]:
            max=data[i]
    return max
def minno(n,data):
    min=data[0]
    for i in range(n):
        if min>data[i]:
            min=data[i]
    return min
def min_max_reverse(num):
    r=revnum=0
    while num:
        r=num%10
        num//=10
        revnum=revnum*10+r
    return revnum
n=int(input())
data=list(map(int,input().split()))

max=maxno(n,data)#calling first max
maxrev=min_max_reverse(max)#reversing the max 
min=minno(n,data)#calling first min
minrev=min_max_reverse(min)#reversing the min

for i in range(n):#assigning supermax and min values to data
    if data[i]==max:
        data[i]=maxrev
    if data[i]==min:
        data[i]=minrev
supermax=maxno(n,data)#calling max of modified datalist 
supermin=minno(n,data)#calling min of modified datalist
if supermax==maxrev:
    print("super max")
else:
    print("not supermax")
if supermin==minrev:
    print("super min")
else:
    print("not supermin")