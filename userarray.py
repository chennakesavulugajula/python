r=int(input("enter the number of rows:"))
c=int(input("enter the number of colomns"))
l=[]
for i in range(r):
    m=[]
    for j in range(c):
        v=int(input())
        m.append(v)
    l.append(m)
print(l)