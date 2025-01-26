# def solve(n,arr,dp):
#     if n==0 :
#         return 0
#     if dp[n]!=None:
#         return dp[n]
#     left= abs(arr[n]-arr[n-1])+solve(n-1,arr,dp)
#     right=float('inf')
#     if n>1:
#         right= abs(arr[n]-arr[n-2])+solve(n-2,arr,dp)
#     dp[n]=min(left,right)
#     return dp[n]
# n=int(input())
# arr=list(map(int,input().split()))
# dp=[None]*n
# print(solve(n-1,arr,dp))
# print(dp)

# n=int(input())-1
# arr=list(map(int,input().split()))
# dp=[0]*n
# dp[0]=0
# for i in range(1,n):
#     l=dp[i-1]+abs(arr[i]-arr[i-1])
#     r=float('inf')
#     if i>1:
#         r= dp[n-2]+abs(arr[i]-arr[i-2])
#     dp[i]=min(l,r)
# print(dp)

n=int(input())-1
arr=list(map(int,input().split()))
prev=0
prev1=0
for i in range(1,n):
    l=prev+abs(arr[i]-arr[i-1])
    r=float('inf')
    if i>1:
        r= prev1+abs(arr[i]-arr[i-2])
    curr=min(l,r)
    prev1=prev
    prev=curr
print(prev)