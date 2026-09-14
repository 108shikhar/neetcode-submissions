class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(1,len(nums),1):
            x=nums[i]
            j=i-1
            while j>=0:
                if nums[j]<x:
                    dp[i]=max(dp[i],1+dp[j])
                j=j-1
        return max(dp)