class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[None]*(101)
        n=len(nums)
        i=0
        def solve(i):
            if i>=n:
                return 0
            if dp[i]!=None:
                return dp[i]
            take=(nums[i] + solve(i+2))
            leave=(0 + solve(i+1))
            dp[i]=max(take,leave)
            return dp[i]
        return solve(i)
