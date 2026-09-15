class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n=len(nums)
        m=target
        dp=[0]*(m+1)
        dp[0]=1
        for i in range(1,m+1):
            for j in range(0,n):
                if i>=nums[j]:
                    dp[i]=dp[i]+dp[i-nums[j]]
        return dp[m]