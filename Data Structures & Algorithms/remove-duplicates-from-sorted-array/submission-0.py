class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=0
        j=0
        for key, value in d.items():
            nums[j]=key
            j=j+1
        return j