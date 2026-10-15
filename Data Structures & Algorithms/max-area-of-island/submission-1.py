class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col,ans=len(grid),len(grid[0]),0
        visit=set()
        def dfs(i,j,grid,visit):
            val=(i,j)
            if (i<0 or i>=row) or (j<0 or j>=col)or val in visit or grid[i][j]==0:
                return 0
            visit.add(val)
            area=1
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                area=area+dfs(x,y,grid,visit)
            return area
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (i,j) not in visit:
                    ans=max(ans,dfs(i,j,grid,visit))
        return ans