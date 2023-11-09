'''def find_count(n):
    if n<=1:
        return n
    else:
        return find_count(n-1)+find_count(n-2)
n=int(input("Enter the number of stairs:"))
print("nuber of ways:",find_count(n+1))
l=list(map(int,input().split()))
n=int(input())
print(l)
a=l[n:]
b=l[:n]
print(a+b)
a1=list(map(int,input().split()))
print(a1)
a2=list(map(int,input().split()))
print(a2)
count=0
for i in range(len(a2)):
    if a2[i] in a1:
        count+=1
if(count==len(a2)):
    print("Yes")
else:
    print("no")'''
l=list(map(int,input().split()))
k=int(input())
maximum=max(l)
print(maximum-k)
    

        
