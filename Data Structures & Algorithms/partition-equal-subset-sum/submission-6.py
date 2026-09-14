class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        val=0
        for i in nums:
            val=val+i
        if val%2!=0:
            return False
        target=val//2
        dp=[[None for c in range(target+1)] for r in range(len(nums)+1)]
        def solve(i,t):
            if t==0:
                return True
            if i<0:
                return False
            if i==0 and nums[i]==t:
                return True
            if dp[i][t]!=None:
                return dp[i][t]
            if nums[i]<=t:
                pick=solve(i-1,t-nums[i])
            else:
                pick=False
            notpick=solve(i-1,t)
            dp[i][t]=pick or notpick
            return dp[i][t]
        return solve((len(nums)-1),target)