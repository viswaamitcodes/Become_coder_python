n=int(input())
data=list(map(int,input().split()))
rotate=int(input())
def rotate_list(n,data,rotate):
    if rotate>len(data):
        rotate%=len(data)
    for i in data[:rotate]:
        data.remove(i)
        data.append(i)    
    print(*data)
rotate_list(n,data,rotate)