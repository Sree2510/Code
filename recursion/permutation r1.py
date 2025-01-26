# def sol(n,arr,ans,k,ref):
#     if len(ref)==n:
#         ans.append(ref[:])
#         return
#     for i in range(n):
#         if k[i]==None:
#             k[i]=1
#             ref.append(arr[i])
#             sol(n,arr,ans,k,ref)
#             k[i]=None
#             ref.pop(-1)
#
# n=int(input())
# arr=list(map(int,input().split()))
# k=[None]*n
# ref=[]
# ans=[]
# sol(n,arr,ans,k,ref)
# print(ans)

def solve(n,arr,i,ans):
    if i==n:
        ans.append(arr[:])
        return
    for _ in range(i,n,1):
        arr[_],arr[i]=arr[i],arr[_]
        solve(n,arr,i+1,ans)
        arr[_], arr[i] = arr[i], arr[_]

n=int(input())
arr=list(map(int,input().split()))
ans=[]
solve(n,arr,0,ans)
print(ans)