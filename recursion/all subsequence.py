def recursion(n,i,ref,arr,k):
    if i>=n:
        if sum(ref)==k:
            print(ref)
        return
    recursion(n,i+1,ref,arr,k)
    ref.append(arr[i])
    recursion(n,i+1,ref,arr,k)
    ref.pop(-1)

n=int(input())
arr=sorted(list(map(int,input().split())))
k=int(input())
sol=set()
ref=[]
recursion(n,0,ref,arr,k)