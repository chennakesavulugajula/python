a=list(map(str,input("enter the input strings:").split()))
sum=0
print(a)
for i in a:
    if i.isdigit()==True:
        sum+=int(i)
        print(sum)
