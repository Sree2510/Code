from collections import deque
def sol(x,y,t1,t2):
    if x==t1 and y==t2:
        return 0
    moves=[(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2),(1, -2), (-1, 2), (-1, -2)]
    solution=[[False ]*8 for i in range(8)]
    solution[x][y]=True
    queue=deque([(x,y,0)])
    while queue:
        x1,y1,count=queue.popleft()
        for i,j in moves:
            r,c=x1+i,y1+j
            if 0<=r<8 and 0<=c<8 and not solution[r][c]:
                if r==t1 and c==t2:
                    return count+1
                solution[r][c]=True
                queue.append((r,c,count+1))
    return -1


x=int(input())-1
y=int(input())-1
t1=int(input())-1
t2=int(input())-1
n=8
print(sol(x,y,t1,t2))
