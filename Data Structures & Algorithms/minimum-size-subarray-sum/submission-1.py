class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,val=0,0
        ans=float('inf')
        for r in range(0,len(nums),1):
            val=val+nums[r]
            while val>=target:
                val=val-nums[l]
                ans=min(ans,(r-l+1))
                l=l+1
            r=r+1
        if ans==float('inf'):
            return 0
        else:
            return ans

