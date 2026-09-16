class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[None for c in range(n)] for r in range(m)]
        def path(i,j):
            if i==0 and j==0:
                return grid[0][0]
            if i<0 or j<0:
                return 201
            if dp[i][j]!=None:
                return dp[i][j]
            up=path(i-1,j)
            left=path(i,j-1)
            dp[i][j]=grid[i][j]+min(up,left)
            return dp[i][j]
        return path(m-1,n-1)