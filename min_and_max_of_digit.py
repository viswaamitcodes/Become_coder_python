n=input()
min=int(n[0])
max=int(n[0])
for i in n:
    i=int(i)
    if (i>max):
        max=i
    if (i<min):
        min=i
print(min,max)
