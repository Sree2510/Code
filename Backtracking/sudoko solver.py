def is_valid(row,col,key,board):
    for i in range(9):
        if board[i][col]==key:
            return False
        if board[row][i]==key:
            return False
        if board[3*(row//3)+i//3][3*(col//3)+i%3]==key:
            return False
    return True

def solve(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==".":
                for _ in map(str,range(1,10)):
                    if is_valid(i,j,_,board):
                        board[i][j]=_
                        if solve(board):
                            return True
                        else:
                            board[i][j]="."
                return False
    return True

board=[]
for i in range(9):
    board.append(list(map(str,input().split())))
solve(board)
for i in board:
    print(i)

"""
5 3 . 6 7 8 9 . 2
6 7 2 1 9 5 3 4 8
. 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 . 4 8 . 6
9 6 . 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
"""