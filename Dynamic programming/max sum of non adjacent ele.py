# Recursion and memoization

# def solve(a,ind,dp):
#     if ind==0:
#         return a[ind]
#     if ind<0:
#         return 0
#     if dp[ind]!=-1:
#         return dp[ind]
#     p=a[ind]+solve(a,ind-2,dp)
#     np=0+solve(a,ind-1,dp)
#     dp[ind]= max(p,np)
#     return dp[ind]
# a=[2,1,4,9]
# dp=[-1 for i in range(len(a))]
# print(solve(a,len(a)-1,dp))

# Tabulation

# a=[2,1,4,9]
# dp=[-1 for i in range(len(a))]
# dp[0]=a[0]
# n=0
# for i in range(1,len(a)):
#     p=a[i]
#     if i>1:
#         p+=dp[i-2]
#     np= 0+dp[i-1]
#     dp[i]=max(p,np)
# print(dp[-1])

# space optimization

a=[2,1,4,9]
dp=[-1 for i in range(len(a))]
prev=a[0]
prev1=0
for i in range(1,len(a)):
    p=a[i]
    if i>1:
        p+=prev1
    np= 0+prev
    curr=max(p,np)
    prev1=prev
    prev=curr
print(prev)