class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp=[[None for c in range(n)] for r in range(m)]
        def grid(i,j):
            if obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=None:
                return dp[i][j]
            up=grid(i-1,j)
            left=grid(i,j-1)
            dp[i][j]=up+left
            return dp[i][j]
        return grid(m-1,n-1)