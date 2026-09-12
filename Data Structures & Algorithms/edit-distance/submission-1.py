class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp=[[None for c in range(n+1)] for r in range(m+1)]
        i,j=m,n
        def solve(i,j):
            if i==0 and j==0:
                return 0
            if i==0 and j>0 or i>0 and j==0:
                return abs(i-j)
            if dp[i][j]!=None:
                return dp[i][j]
            if word1[i-1]==word2[j-1]:
                dp[i][j]=0+solve(i-1,j-1)
            else:
                dp[i][j]=1+min(solve(i-1,j),solve(i,j-1),solve(i-1,j-1))
            return dp[i][j]
        val=solve(i,j)
        return val