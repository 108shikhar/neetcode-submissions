class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[None]*(n+1)
        i=n
        def solve(i):
            if i==2:
                return 1
            if dp[i]!=None:
                return dp[i]
            dp[i]=1
            for x in range(2,i,1):
                y=i-x
                ans=max((x*y),(x*solve(y)))
                dp[i]=max(dp[i],ans)
            return dp[i]
        return solve(i)
