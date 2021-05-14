
n=input()
max=int(n[0])
min=int(n[0])
c=p=0
for i in n:
    i=int(i)
    if (i>max):
        max=i
        c=1
    elif (max==i):
        c+=1
    if (i<min):
        min=i
        p=1
    elif (min==i):
        p+=1
print(min,max)
print("min count:",p,"max count:",c)
