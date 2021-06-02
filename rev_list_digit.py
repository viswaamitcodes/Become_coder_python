def rev_lst_digit(n,data):
    count=0
    digit=0
    for i in data:
        while i:
            r=i%10
            i//=10
            digit=digit*10+r
        data[count]=digit
        count+=1
        digit=0
n=int(input())
data=list(map(int,input().split()))
rev_lst_digit(n,data)
print(*data)