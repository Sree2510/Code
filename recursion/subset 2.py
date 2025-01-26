# def recursion(n,arr,i,sol,ref):
#     if i==n:
#         if ref in sol:
#             return
#         else:
#             sol.append(ref[:])
#         return
#     ref.append(arr[i])
#     recursion(n,arr,i+1,sol,ref)
#     ref.pop(-1)
#     recursion(n,arr,i+1,sol,ref)
#
# arr=list(map(int,input().split()))
# n=len(arr)
# sol=[]
# ref=[]
# recursion(n,arr,0,sol,ref)
# print(sorted(sol))

def recursion(n,i,arr,sol,ref):
    sol.append(ref[:])
    for _ in range(i,n-1):
        if _!=i and arr[_]==arr[_-1]:
            continue
        ref.append(arr[_])
        recursion(n,_+1,arr,sol,ref)
        ref.pop(-1)


n=int(input())
arr=list(map(int,input().split()))
sol=[]
ref=[]
recursion(n,0,arr,sol,ref)
print(sol)