def ways(i):
    if i==0:
        return 1
    if i==1:
        return 1
    return ways(i-1)+ways(i-2)
n=int(input())
prev=1
prev1=2
for _ in range(2,n):
    c=prev+prev1
    prev=prev1
    prev1=c
print(prev1)
print(ways(n))
