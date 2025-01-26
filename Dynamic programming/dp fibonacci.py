a=int(input())
prev=0
prev1=1
for i in range(2,a+1):
    temp=prev+prev1
    prev=prev1
    prev1=temp
print(prev1)