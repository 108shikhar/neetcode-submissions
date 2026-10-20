class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row,col,opn=len(board),len(board[0]),set()
        def dfs(x,y):
            if board[x][y]=="X":
                return
            else:
                opn.add((x,y))
                for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if (i>=0 and i<row) and (j>=0 and j<col) and (i,j) not in opn:
                        dfs(i,j)
        for c in range(col):
            dfs(0,c)
            dfs(row-1,c)
        for r in range(row):
            dfs(r,0)
            dfs(r,col-1)
        for i in range(row):
            for j in range(col):
                if (i,j) not in opn and board[i][j]=="O":
                    board[i][j]="X"