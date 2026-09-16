class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1,-1] for r in range(n)]
        def solve(i,j):
            if i>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if j==1:
                buy=(-prices[i]+solve(i+1,0))
                notbuy=(0+solve(i+1,1))
                profit=max(buy,notbuy)
            if j==0:
                sell=(prices[i]+solve(i+2,1))
                notsell=(0+solve(i+1,0))
                profit=max(sell,notsell)
            dp[i][j]=profit
            return dp[i][j]
        return solve(0,1)