n=int(input())
data=list(map(int,input().split()))
def max_sort(n,data):
    arr_len=c=0
    for i in range(n-1):
        c+=1
        if data[i]>data[i+1] :
            if arr_len<c :
                arr_len=c
            c=0
    if c>arr_len: 
        arr_len=c+1 
    return arr_len
print(max_sort(n,data))