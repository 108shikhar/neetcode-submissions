class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        col=len(grid[0])
        row=len(grid)
        visit=set()
        res=0
        def dfs(i,j,grid,visit):
            nonlocal res
            val=(i,j)
            visit.add(val)
            for x,y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                if (x,y) not in visit:
                    if x<0 or x>=row or y<0 or y>=col:
                        res=res+1
                    elif grid[x][y]==0:
                        res=res+1
                    elif grid[x][y]==1:
                        val=(x,y)
                        visit.add(val)
                        dfs(x,y,grid,visit)
            return res
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (i,j) not in visit:
                    dfs(i,j,grid,visit)
        return res