n=input()
data=n.split()
m=len(data[0])
val=data[0]
for i in data:
    if m < len(i):
        m=len(i)
        val=i
print(f"{data.index(val)+1} {val} {m}")