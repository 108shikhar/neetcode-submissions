class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l,r=0,1
        while (r-l)<(k+1) and r<len(nums):
            if nums[l]==nums[r]:
                return True
            if (r-l)==k:
                l=l+1
                r=l
            r=r+1
        return False