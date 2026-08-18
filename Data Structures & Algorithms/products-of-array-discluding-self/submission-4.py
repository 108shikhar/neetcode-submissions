class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        prefix=1
        suffix=1
        for i in range(0, len(nums), 1):
            a.append(prefix)
            prefix=prefix*nums[i]
        j=len(nums)-1
        while j>=0:
            b.append(suffix)
            suffix=suffix*nums[j]
            j=j-1
        b.reverse()
        c=[]
        for l in range(0, len(nums), 1):
            x=a[l]*b[l]
            c.append(x)
        return c