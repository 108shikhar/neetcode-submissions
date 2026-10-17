class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            j=i+1
            while j<len(nums):
                if nums[j]==nums[i] and (j-i)<=k:
                    return True
                else:
                    j=j+1
        return False