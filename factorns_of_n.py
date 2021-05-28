from math import *
# n=int(input())
# def factorcount(num,i):
#     k=1
#     if i>int(sqrt(num)):
#         return 
#     if num%i==0 and num//i==0:
#         k+=factorcount(num,i)
# num=int(input())
# c=0
# for i in range(1,int(sqrt(num))+1):
#     c+=factorcount(num,i)

# print(c)
num=int(input())
k=0
for i in range(1,int(sqrt(num)+1)):
    if num%i==0:
        k+=1
        if i!=num//i:
            k+=1
print(k)
