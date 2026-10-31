class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 1
        i,j=0,1
        while j<n:
            if nums[i]==nums[j]:
                j=j+1
            elif nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i,j=i+1,j+1
        return i+1