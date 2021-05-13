n=input()
d,e=0,0
num=""
for i in n:
        if i==n[0]:
            d=i
        if (i>=n[1] and i<n[-1]):
            num+=i
        if i==n[-1]:
            e=n[-1]
print(f"{e}{num}{d}")


