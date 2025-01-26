# def recursion(n,i,ref,arr,k):
#     if i>=n:
#         if sum(ref)==k:
#             print(ref)
#         return
#     recursion(n,i+1,ref,arr,k)
#     ref.append(arr[i])
#     recursion(n,i+1,ref,arr,k)
#     ref.pop(-1)
#
# n=int(input())
# arr=sorted(list(map(int,input().split())))
# k=int(input())
# sol=set()
# ref=[]
# recursion(n,0,ref,arr,k)

# def s(n,i,arr,sum,t):
#     if (i>=n):
#         if sum==t:
#             return 1
#         return 0
#     sum+=arr[i]
#     l=s(n,i+1,arr,sum,t)
#     sum-=arr[i]
#     r=s(n,i+1,arr,sum,t)
#     return l+r
# n=int(input())
# arr=sorted(list(map(int,input().split())))
# t=int(input())
# ref=[]
# print(s(n,0,arr,0,t))

# def recursion(n,arr,i,target,sol,ref):
#     if (i==n):
#         if target==0:
#             sol.append(ref[:])
#         return
#
#     if arr[i]<=target:
#         ref.append(arr[i])
#         recursion(n,arr,i,target-arr[i],sol,ref)
#         ref.pop(-1)
#     recursion(n,arr,i+1,target,sol,ref)
#
#
# n=int(input())
# arr=list(map(int,input().split()))
# target=int(input())
# sol=[]
# ref=[]
# recursion(n,arr,0,target,sol,ref)
# for i in sol:
#     print(i)



# def recursion(n,arr,i,target,sol,ref):
#     if target==0:
#         sol.append(ref[:])
#         return
#     for _ in range(i,n):
#         if _>i and arr[_]==arr[_-1]:
#             continue
#         if arr[_]>target:
#             break
#         ref.append(arr[_])
#         recursion(n,arr,_+1,target-arr[_],sol,ref)
#         ref.pop(-1)
#
# for i in range(int(input())):
#     n=int(input())
#     arr=sorted(list(map(int,input().split())))
#     target=int(input())
#     sol=[]
#     ref=[]
#     recursion(n,arr,0,target,sol,ref)
#     if len(sol)==0:
#         print()
#         print("Empty")
#     else:
#         for i in sol:
#             print(i)

# def recursion(n,arr,i,sol,sum):
#     if i==n:
#         sol.append(sum)
#         return
#     sum+=arr[i]
#     recursion(n,arr,i+1,sol,sum)
#     sum-=arr[i]
#     recursion(n,arr,i+1,sol,sum)
#
# n=int(input())
# arr=list(map(int,input().split()))
# sol=[]
# recursion(n,arr,0,sol,0)
# print(sorted(sol))
# print(sol)

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