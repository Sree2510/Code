def s(n,i,arr,sum,t):
    if (i>=n):
        if sum==t:
            return 1
        return 0
    sum+=arr[i]
    l=s(n,i+1,arr,sum,t)
    sum-=arr[i]
    r=s(n,i+1,arr,sum,t)
    return l+r
n=int(input())
arr=sorted(list(map(int,input().split())))
t=int(input())
ref=[]
print(s(n,0,arr,0,t))