class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[0 for c in range(amount+1)] for r in range(len(coins)+1)]
        n=len(coins)
        s=amount
        def solve(coins,n,s):
            for i in range(n+1):
                dp[i][0]=1
                
            for i in range(1, n+1):
                for j in range(1, s+1):
                    
                    dp[i][j]=dp[i-1][j]
                    if j>=coins[i-1]:
                        dp[i][j]=dp[i][j]+dp[i][j-coins[i-1]]
                        
            return dp[n][s]
            
        return solve(coins,n,s)