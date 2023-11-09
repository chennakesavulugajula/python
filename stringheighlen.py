a=list(map(str,input("enter the input strings:").split()))
b=[]
print(a)
for i in a:
    k=len(i)
    b.append(k)
print(max(b),i)
