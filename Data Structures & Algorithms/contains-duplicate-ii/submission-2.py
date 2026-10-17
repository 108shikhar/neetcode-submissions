class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for l in range(len(nums)-1):
            r=l+1
            while r<len(nums):
                if nums[r]==nums[l] and abs(r-l)<=k:
                    return True
                r=r+1
        return False