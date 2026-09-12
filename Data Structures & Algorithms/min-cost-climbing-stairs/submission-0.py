class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        s=len(cost)
        dp=[None]*100
        def solve(n):
            if n>=s:
                return 0
            if dp[n]!=None:
                return dp[n]
            val=cost[n]
            dp[n]=val+min(solve(n+1),solve(n+2))
            return dp[n]
        return min(solve(0),solve(1))