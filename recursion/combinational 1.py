def recursion(n,arr,i,target,sol,ref):
    if (i==n):
        if target==0:
            sol.append(ref[:])
        return

    if arr[i]<=target:
        ref.append(arr[i])
        recursion(n,arr,i,target-arr[i],sol,ref)
        ref.pop(-1)
    recursion(n,arr,i+1,target,sol,ref)


n=int(input())
arr=list(map(int,input().split()))
target=int(input())
sol=[]
ref=[]
recursion(n,arr,0,target,sol,ref)
for i in sol:
    print(i)
