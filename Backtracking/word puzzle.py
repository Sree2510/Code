# """
# input 1:
# 2
# ABCCED
# ABCB
# output 2:
# True
# False
# input 2:
# 4
# BICSI
# BIE
# ZOHO
# SEE
# output 2:
# True
# False
# False
# True
# """

def solve(x,y,word,target,visited,index=0):
    if index==len(target):
        return True
    moves=[(0,1),(1,0),(-1,0),(0,-1)]
    for dx,dy in moves:
        x1,y1=x+dx,y+dy
        if 0<=x1<len(word) and 0<=y1<len(word[0]) and not visited[x1][y1]:
            if word[x1][y1]==target[index]:
                visited[x1][y1]=True
                if solve(x1,y1,word,target,visited, index+1):
                    return True
            visited[x1][y1]=False
    return False



a=int(input())
word=[['A','B','C','I'],
      ['B','I','C','S'],
      ['C','D','E','E']]
for _ in range(a):
    target=input().upper()
    found=False
    visited=[[False for _ in range(len(word[0]))] for _ in range(len(word))]
    for i in range(len(word)):
        for j in range(len(word[0])):
            if word[i][j]==target[0]:
                visited[i][j]=True
                if solve(i,j,word,target,visited,1):
                    found=True
                    break
                visited[i][j]=False
        if found:
            break
    print("True" if found else "False")


