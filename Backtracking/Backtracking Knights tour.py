# def sol(x, y, solution, count):
#     global m, found, k
#     if x == t1  and y == t2  and solution[x][y]==0:
#         solution[x][y] = count
#         found = True
#         if count < m:
#             m = count
#             for i in range(n):
#                 best_solution[i]=solution[i][:]
#         return False
#
#     if x >= 0 and x < n and y >= 0 and y < n and solution[x][y] == 0 and k[x][y]==False:
#         k[x][y]=True
#         solution[x][y] = count
#         if sol(x + 2, y + 1, solution, count + 1):
#             return True
#         if sol(x + 1, y + 2, solution, count + 1):
#             return True
#         if sol(x - 1, y + 2, solution, count + 1):
#             return True
#         if sol(x - 2, y + 1, solution, count + 1):
#             return True
#         if sol(x - 2, y - 1, solution, count + 1):
#             return True
#         if sol(x - 1, y - 2, solution, count + 1):
#             return True
#         if sol(x + 1, y - 2, solution, count + 1):
#             return True
#         if sol(x + 2, y - 1, solution, count + 1):
#             return True
#         return False
#     return False
# a = int(input())-1
# b = int(input())-1
# t1 = int(input())-1
# t2 = int(input())-1
# n = 8
# solution = [[0 for i in range(n)] for i in range(n)]
# best_solution = [[0 for i in range(n)] for i in range(n)]
# k = [[False for i in range(n)] for i in range(n)]
# m = float('inf')
# found = False
# sol(a, b , solution, 0)
# for i in k:
#     print(i)
# for i in solution:
#     print(i)
# print("  ")
# for i in best_solution:
#     print(i)
# print(m)


#
# global path_x,path_y,n
# n=8
# path_x=[2,1,-1,-2,-2,-1,1,2]
# path_y=[1,2,2,1,-1,-2,-2,-1]
# k=0
#
#
# def sol(solution,row,col,step):
#     if step==n**2:
#         return True
#
#     for i in range(n):
#         row_new=row+path_x[i]
#         col_new=col+path_y[i]
#
#         if valid(solution,row_new,col_new):
#             solution[row_new][col_new]=step
#
#             if sol(solution,row_new,col_new,step+1):
#                 return True
#
#             solution[row_new][col_new]=-1
#     return False
#
# def valid(solution,x,y):
#     if 0<=x<n and 0<=y<n and solution[x][y]==-1:
#         return True
#     return False
# a=int(input())-1
# b=int(input())-1
# t0=int(input())-1
# t1=int(input())-1
#
# solution=[[-1 for i in range(n)]for i in range(n)]
# solution[0][0]=0
# step=1
# if sol(solution,0,0,step):
#     for i in solution:
#         print(i)
# else:
#     print("No solution exists")


# def is_valid(x,y,solution,visited):
#     if 0<=x<n and 0<=y<n and solution[x][y]==-1 and visited==False:
#         return True
#     return False
#
# def sol(x,y,solution,count,visited):
#     global m,k,moves,found,n,t1,t2
#
#     solution[x][y]=count
#     visited[x][y]=True
#     if count==(n*n)-1:
#         found=True
#         return True
#     if x==t1 and y==t2:
#         m=count-1
#         for _ in range(n):
#             k[_]=solution[_][:]
#     for newx,newy in moves:
#         x1,y1=x+newx,y+newy
#         if is_valid(x1,y1,solution,visited):
#             if sol(x1,y1,solution,count+1,visited):
#                 return True
#     solution[x][y]=-1
#     visited[x][y]=False
#     return False
#
# n=8
# found=False
# moves=[(1,2),(2,1),(1,-2),(-1,2),(-2,1),(2,-1),(-1,-2),(-2,-1)]
# solution=[[-1 for _ in range(n)] for _ in range(n)]
# visited=[[False for _ in range(n)] for _ in range(n)]
# k=[[0 for _ in range(n)] for _ in range(n)]
# m=float('inf')
# a=int(input())-1
# b=int(input())-1
# t1=int(input())-1
# t2=int(input())-1
# solution[a][b]=0
# count=1
# sol(a,b,solution,count,visited)
# for i in k:
#     print(i)
# print(" ")
# for i in solution:
#     print(i)
# print(m)
# if found:
#     print(m)
# else:
#     print("No solution exists")



from collections import deque

class KnightWorld:
    class Node:
        def __init__(self, row, col, step):
            self.row = row
            self.col = col
            self.step = step

    @staticmethod
    def find_out(r1, c1, r2, c2):
        if r1 == r2 and c1 == c2:
            return 0
        directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        valid = [[False for _ in range(8)] for _ in range(8)]
        valid[r1][c1] = True
        queue = deque([KnightWorld.Node(r1, c1, 0)])
        while queue:
            temp = queue.popleft()
            for dir in directions:
                r, c = temp.row + dir[0], temp.col + dir[1]
                if 0 <= r < 8 and 0 <= c < 8 and not valid[r][c]:
                    if r == r2 and c == c2:
                        return temp.step + 1
                    valid[r][c] = True
                    queue.append(KnightWorld.Node(r, c, temp.step + 1))
        return -1

    @staticmethod
    def main():
        s = input("Enter the starting and ending positions (space-separated, 1-8):\n")
        r1, c1, r2, c2 = map(int, s.split())
        # Adjust for 0-based indexing
        r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
        print(KnightWorld.find_out(r1, c1, r2, c2))

if __name__ == "__main__":
    KnightWorld.main()
