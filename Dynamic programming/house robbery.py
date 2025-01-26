# def solve(value):
#     prev=value[0]
#     prev1=0
#     for _ in range(1,len(value)):
#         p=value[_]
#         if _>1:
#             p+=prev1
#         np=0+prev
#         current=max(p,np)
#         prev1=prev
#         prev=current
#     return prev
#
# for i in range(int(input())):
#     a=int(input())
#     arr=list(map(int,input().split()))
#     if len(arr)==1:
#         print(*arr)
#     else:
#         temp1=[arr[_] for _ in range(a-1)]
#         temp2 = [arr[_] for _ in range(1,a)]
#         t1=solve(temp1)
#         t2=solve(temp2)
#         print(max(t1,t2))

a=list(map(int,input().split()))
p,np=0,0
for i in a:
    r=np+i
    nr=max(p,np)
    p,np=r,nr
print(max(p,np))