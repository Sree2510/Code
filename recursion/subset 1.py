def recursion(n,arr,i,sol,sum):
    if i==n:
        sol.append(sum)
        return
    sum+=arr[i]
    recursion(n,arr,i+1,sol,sum)
    sum-=arr[i]
    recursion(n,arr,i+1,sol,sum)

n=int(input())
arr=list(map(int,input().split()))
sol=[]
recursion(n,arr,0,sol,0)
print(sorted(sol))
print(sol)