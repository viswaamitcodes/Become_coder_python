from math import *
left=int(input())
right=int(input())
prime=0
for i in range(left,right+1):
    bits=bin(i)
    count=0
    count2=False
    for j in bits:
        if j=="1":
            count+=1
    for k in range(2,count):
        if (count % k) == 0:
            count2 = True
            break
    if count2==False and count!=1:
        prime+=1
print(prime)

