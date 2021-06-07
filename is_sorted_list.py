n=int(input())
data=list(map(int,input().split()))
def is_sorted(n,data):
    lis=data.copy()
    data.sort()
    if data == lis:
        return True
    else:
        data.sort(reverse=True)
        if data == lis:
            return True
        else:
            return False
print(is_sorted(n,data))