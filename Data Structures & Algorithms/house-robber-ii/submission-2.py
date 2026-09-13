class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp=[None]*100
        a=nums[:-1:1]
        b=nums[1::1]
        i=0
        def solve(i,n,arr):
            if i>=n:
                return 0
            if dp[i]!=None:
                return dp[i]
            take=arr[i]+solve(i+2,n,arr)
            leave=0+solve(i+1,n,arr)
            dp[i]=max(take,leave)
            return dp[i]
        ans1=solve(i,len(a),a)
        dp=[None]*100
        ans2=solve(i,len(b),b)
        return max(ans1,ans2)