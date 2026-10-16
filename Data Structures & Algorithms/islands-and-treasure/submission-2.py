class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        q=deque()
        row,col=len(grid),len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    val=[r,c]
                    q.append(val)      
        while q:
            out=q.popleft()
            x,y=out[0],out[1]
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if (i>=0 and i<row) and (j>=0 and j<col) and grid[i][j]!=-1:
                    if grid[i][j]!=0 and grid[i][j]>grid[x][y]+1:
                        grid[i][j]=grid[x][y]+1
                        val=[i,j]
                        q.append(val) 