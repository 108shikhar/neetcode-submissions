class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        ans,res=0,0
        visit=set()
        def dfs(i,j,grid,visit):
            nonlocal res
            res=res+1
            val=(i,j)
            visit.add(val)
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if (x,y) not in visit and (x>=0 and x<row) and (y>=0 and y<col):
                    if grid[x][y]==1:
                        dfs(x,y,grid,visit)
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (i,j) not in visit:
                    dfs(i,j,grid,visit)
                    ans=max(ans,res)
                    res=0
        return ans