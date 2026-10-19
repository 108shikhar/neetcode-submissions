class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q,time,fresh=deque(),0,0
        row,col=len(grid),len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append([r,c])
                elif grid[r][c]==1:
                    fresh=fresh+1
        while q and fresh>0:
            ans=len(q)
            for i in range(ans):
                val=q.popleft()
                x,y=val[0],val[1]
                for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if (i>=0 and i<row) and (j>=0 and j<col) and grid[i][j]==1:
                        grid[i][j]=2
                        q.append([i,j])
                        fresh=fresh-1
            time=time+1
        return time if fresh==0 else -1
        