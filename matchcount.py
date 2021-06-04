n=int(input())
data=list(map(int,input().split()))
def matchcount(n,data):
    nums=[]
    c=0
    for i in data:
        if i not in nums:
            nums.append(i)
    for k in range(len(nums)):
        if data[k]==nums[k]:
            c+=1
    return nums,c
nums,c=matchcount(n,data)
print(*nums)
print(c)
