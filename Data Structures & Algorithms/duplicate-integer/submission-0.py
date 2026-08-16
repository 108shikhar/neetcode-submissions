class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a={}
        for i, j in enumerate(nums):
            x=nums[i]
            if x not in a:
                a[x]=1
            elif x in a:
                a[x]=a[x]+1
        for key, value in a.items():
            if a[key]>1:
                return True
        return False