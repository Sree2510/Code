def recursion(n,arr,i,target,sol,ref):
    if target==0:
        sol.append(ref[:])
        return
    for _ in range(i,n):
        if _>i and arr[_]==arr[_-1]:
            continue
        if arr[_]>target:
            break
        ref.append(arr[_])
        recursion(n,arr,_+1,target-arr[_],sol,ref)
        ref.pop(-1)

for i in range(int(input())):
    n=int(input())
    arr=sorted(list(map(int,input().split())))
    target=int(input())
    sol=[]
    ref=[]
    recursion(n,arr,0,target,sol,ref)
    if len(sol)==0:
        print()
        print("Empty")
    else:
        for i in sol:
            print(i)