n=input()
c=0
for i in n:
    if i!=" ":
        c+=1
    else:
        print(c,end=" ")
        c=0
print(c)