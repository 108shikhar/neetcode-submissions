class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            y=target-x
            if y in nums:
                j=nums.index(y)
                if j!=i:
                    return [i,j] if i<j else [j,i]