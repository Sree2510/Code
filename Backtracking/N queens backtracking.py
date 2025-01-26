# def safe(row,col,board,n):
#     r=row
#     c=col
#     while (row>=0 and col>=0):
#         if board[row][col]=="Q":
#             return False
#         row-=1
#         col-=1
#     row=r
#     col=c
#
#     while (col>=0):
#         if board[row][col]=="Q":
#             return False
#         col-=1
#
#     row=r
#     col=c
#
#     while (col>=0 and row<n):
#         if board[row][col]=="Q":
#             return False
#         col-=1
#         row+=1
#
#     return True
#
# def solve(c,n,board,ans):
#     if c==n:
#         for i in board:
#             ans.append(i[:])
#         return
#     for _ in range(n):
#         if safe(_,c,board,n):
#             board[_][c]="Q"
#             solve(c+1,n,board,ans)
#             board[_][c]=" "
#
# n=int(input())
# board=[[" " for i in range(n)]for i in range(n)]
# ans=[]
# solve(0,n,board,ans)
# for i in ans:
#     print(i)



def solve(col,board,lr,ud,ld,ans,n):
    if col==n:
        for _ in board:
            ans.append(_[:])
        return
    for _ in range(n):
        if lr[_]==0 and ud[(n-1) + col-_]==0 and ld[col+_]==0:
            lr[_]=1
            ld[_+col]=1
            ud[n-1 + col-_]=1
            board[_][col]="Q"
            solve(col+1,board,lr,ud,ld,ans,n)
            lr[_]=0
            ld[_+col]=0
            ud[(n-1)+col-_]=0
            board[_][col]=" "


n=int(input())
board=[[" " for _ in range(n)]for _ in range(n)]
leftrow=[0 for _ in range(n)]
upperdiagonal=[0 for _ in range(2*n-1)]
lowerdiagonal=[0 for _ in range(2*n-1)]
ans=[]
solve(0,board,leftrow,upperdiagonal,lowerdiagonal,ans,n)
for i in ans:
    print(i)

