class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col=len(grid),len(grid[0])
        visit=set()
        ans=0
        def dfs(i,j,grid,visit):
            val=(i,j)
            visit.add(val)
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if (x,y) not in visit:
                    if (x>=0 and x<row) and (y>=0 and y<col):
                        if int(grid[x][y])==1:
                            dfs(x,y,grid,visit)
        for i in range(row):
            for j in range(col):
                if int(grid[i][j])==1 and (i,j) not in visit:
                    dfs(i,j,grid,visit)
                    ans=ans+1
        return ans