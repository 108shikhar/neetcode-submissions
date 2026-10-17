class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val=set(nums)
        if len(val)==len(nums):
            return False
        else:
            return True