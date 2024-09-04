n=int(input())
arr=list(map(int,input().split()))
a=sum(arr)
res=[0]*n
c=0
for i in range (0,n):
    c+=a[i]
    res[i]=abs(c-(a-c))
print(res)
