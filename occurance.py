l=[]
n=int(input())
for i in range(n):
    l.append(input())
s=set(l)
l1=list(s)
for i in l1:
    count=0
    for j in range(0,n):
        if i==l[j]:
            count+=1
    print(i,"=",count);
