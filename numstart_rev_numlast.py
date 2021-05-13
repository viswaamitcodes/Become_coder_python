n=input()
c,q,r,s=0,0,0,0
num=""
num2=0
for i in n:
    if (i>n[0] and i<n[-1]):
        num+=i
    if (i==n[0]):
        q=i
    if (i==n[-1]):
        s=i
c=int(num)
while c:
    r=c%10
    c=c//10
    num2=num2*10+r
print(f"{q}{num2}{s}")
