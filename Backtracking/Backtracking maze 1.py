def sol(x,y,problem,solution,b,count,m=1000):
    if (x==n-1 and y==n-1):
        solution[x][y]=1
        a=1
        if count<m:
            m=count
            for _ in range(len(solution)):
                b[_]=solution[_][:]
            return True
        return False

        return True
    if (x>=0 and x<=n-1) and (y>=0 and y<=n-1) and(solution[x][y]==0) and (problem[x][y]==0):
        solution[x][y]=1
        if (sol(x+1,y,problem,solution,b,count+1)==True):
            return True
        if (sol(x,y+1,problem,solution,b,count+1)==True):
            return True
        if (sol(x-1,y,problem,solution,b,count+1)==True):
            return True
        if (sol(x,y-1,problem,solution,b,count+1)==True):
            return True
        solution[x][y]=0
        return False
    return False
n=5
a=0
b=[[None for _ in range(n)]for _ in range(n)]
problem=[[0,0,0,0,0],
         [1,1,0,1,1],
         [0,0,1,1,1],
         [0,1,1,1,1],
         [0,0,0,0,0]]
if problem[n-1][n-1]==1:
    print("None")
else:
    solution=[[0 for _ in range(n)] for _ in range(n)]
    k=sol(0,0,problem,solution,b,1)
    if k:
        print("Minimum steps:")
        for _ in b:
            print(*_)
    else:
        print("None1")