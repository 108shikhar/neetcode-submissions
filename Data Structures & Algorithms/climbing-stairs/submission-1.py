class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[None]*(n+1)
        def solve(n):
            if n<0:
                return 0
            if n==0:
                return 1
            if dp[n]!=None:
                return dp[n]
            dp[n]=solve(n-1)+solve(n-2)
            return dp[n]
        return solve(n)