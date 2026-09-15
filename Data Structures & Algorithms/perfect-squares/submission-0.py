class Solution:
    def numSquares(self, n: int) -> int:
        a=[]
        i=1
        while i*i<=n:
            a.append(i*i)
            i=i+1
        dp=[n+1]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for j in a:
                if j<=i:
                    dp[i]=min(dp[i],1+dp[i-j])
        return dp[n]